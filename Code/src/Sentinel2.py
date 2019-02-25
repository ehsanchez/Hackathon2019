"""
This code aims to create a data pipeline to provide Sentinel-2 time series.
It is mainly based on tf.data.Dataset object
"""

import tensorflow as tf


class TimeSeries(object):
    def __init__(self, filenames, dimensions=[512, 512, 4 * 12], threshold_value=4095):
        """
        Creates a time series dataset using filenames

        :param filenames: (list) List of tfrecord paths
        :param dimensions: (list) Dimensions of the time series [heigh, width, channels * number of frames]
        :param threshold_value: (int) Max pixel value in time series
        """
        self.filenames = filenames
        self.dimensions = dimensions
        self.threshold_value = threshold_value

    def normalize(self, time_series):
        """
        Reshapes and normalizes the tensor

        :param time_series: (tf.Tensor) Time series tensor
        """
        time_series = tf.reshape(time_series, self.dimensions)
        time_series = tf.clip_by_value(time_series, 0, self.threshold_value)
        time_series = (time_series / (self.threshold_value / 2.0)) - 1

        return time_series

    def decode_fn(self, serialized_example):
        """
        Decodes function for tf.data

        :param serialized_example: (tf.Tensor) An element of the dataset
        """
        features = {'time_series_raw': tf.FixedLenFeature([], tf.string)}
        parsed_features = tf.parse_single_example(serialized_example, features=features)
        time_series = tf.cast(tf.decode_raw(parsed_features['time_series_raw'], tf.float16), tf.float32)
        time_series = self.normalize(time_series)

        return time_series

    def create_dataset(self, batch_size=1, buffer_size=1):
        """
        Creates a dataset of time series

        :param batch_size: (int) Batch size
        :param buffer_size: (int) Buffer size for prefetching data while consuming
        """
        dataset = tf.data.TFRecordDataset(self.filenames)
        dataset = dataset.map(self.decode_fn)
        dataset = dataset.repeat()
        dataset = dataset.batch(batch_size, drop_remainder=True)
        dataset = dataset.prefetch(buffer_size=buffer_size)

        return dataset
