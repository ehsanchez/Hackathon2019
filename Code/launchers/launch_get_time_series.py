import glob
import tensorflow as tf
tf.enable_eager_execution()

import Code.src.Sentinel2 as Sentinel2
import Code.src.utils as utils


# Recover the tfrecords and create a dataset of time series
filenames = glob.glob("/home/eduardo.sanchez/Data/hackathon-isae-2019/training/*.tfrecords")
data = Sentinel2.TimeSeries(filenames=filenames)
dataset = data.create_dataset()

# Get some samples from the dataset
for i, time_series in enumerate(dataset):
    # Get a numpy time series
    np_time_series = time_series.numpy()

    # Create a gif
    utils.display_time_series(np_time_series, i)

    if i == 10: break