"""
This code aims to read the test data which is composed of an image dataset and a patch dataset
"""

import tensorflow as tf


class Datasets(object):
    def __init__(self, image_filename, patch_filename):
        """
        Creates the test dataset

        :param image_filename: (list) Tfrecord path containing the images of shape 512 x 512 x 4
        :param patch_filename: (list) Tfrecord path containing the patches of shape 64 x 64 x 4
        """
        self.image_filename = image_filename
        self.patch_filename = patch_filename

    def decode_image_fn(self, serialized_example):
        """
        Decodes function for tf.data

        :param serialized_example: (tf.Tensor) An element of the dataset
        """
        features = {'image_raw': tf.FixedLenFeature([], tf.string),
                    'image_id': tf.FixedLenFeature([], tf.int64)}

        parsed_features = tf.parse_single_example(serialized_example, features=features)
        image = tf.cast(tf.decode_raw(parsed_features['image_raw'], tf.float16), tf.float32)
        image = tf.reshape(image, [512, 512, 4])
        image_id = tf.cast(parsed_features['image_id'], tf.int32)

        return image, image_id

    def decode_patch_fn(self, serialized_example):
        """
        Decodes function for tf.data

        :param serialized_example: (tf.Tensor) An element of the dataset
        """
        features = {'patch_raw': tf.FixedLenFeature([], tf.string),
                    'patch_id': tf.FixedLenFeature([], tf.int64)}

        parsed_features = tf.parse_single_example(serialized_example, features=features)
        patch = tf.cast(tf.decode_raw(parsed_features['patch_raw'], tf.float16), tf.float32)
        patch = tf.reshape(patch, [64, 64, 4])
        patch_id = tf.cast(parsed_features['patch_id'], tf.int32)

        return patch, patch_id

    def create_dataset(self, image_batch_size=1, image_buffer_size=1, patch_batch_size=1, patch_buffer_size=1):
        """
        Creates the datasets of images and patches

        :param image_batch_size: (int) Batch size of images
        :param image_buffer_size: (int) Buffer size for prefetching data while consuming
        :param patch_batch_size: (int) Batch size of patches
        :param patch_buffer_size: (int) Buffer size for prefetching data while consuming
        """
        image_dataset = tf.data.TFRecordDataset(self.image_filename)
        image_dataset = image_dataset.map(self.decode_image_fn)
        image_dataset = image_dataset.batch(image_batch_size)
        image_dataset = image_dataset.prefetch(buffer_size=image_buffer_size)

        patch_dataset = tf.data.TFRecordDataset(self.patch_filename)
        patch_dataset = patch_dataset.map(self.decode_patch_fn)
        patch_dataset = patch_dataset.batch(patch_batch_size)
        patch_dataset = patch_dataset.prefetch(buffer_size=patch_buffer_size)

        return image_dataset, patch_dataset
