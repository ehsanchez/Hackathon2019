import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
tf.enable_eager_execution()

from Code.src.Datasets import Datasets

# Set the tfrecord paths
image_filename = '/home/eduardo.sanchez/Data/Submission/test_images.tfrecords'
patch_filename = '/home/eduardo.sanchez/Data/Submission/test_patches.tfrecords'

# Create datasets
data = Datasets(image_filename=image_filename, patch_filename=patch_filename)

image_dataset, patch_dataset = data.create_dataset(image_batch_size=1,
                                                   image_buffer_size=1,
                                                   patch_batch_size=64,
                                                   patch_buffer_size=64)

# Get some image samples
for i, batch in enumerate(image_dataset):
    images, image_ids = batch

    print(image_ids.numpy())
    plt.imshow(((images.numpy()[0, :, :, :3]+1)*127.5).astype(np.uint8))
    plt.show()

    if i == 5: break

# Get some patch samples
for i, batch in enumerate(patch_dataset):
    patches, patch_ids = batch

    print(patch_ids.numpy())
    plt.imshow(((patches.numpy()[0, :, :, :3]+1)*127.5).astype(np.uint8))
    plt.show()

    if i == 5: break