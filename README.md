# Hackathon2019
ISAE-SUPAERO Hackathon based on image location retrieval

# Data
As explained during the presentation, you will work with Sentinel-2 image time series. The data is provided in [tfrecord format](https://www.tensorflow.org/tutorials/load_data/tf_records) which is a useful format when dealing with large amounts of data. For training your models, we selected 42 tiles containing several regions of interest such as the Amazon rainforest, the Dead Sea, the city of Los Angeles, the Great Sandy Desert, circular fields in Saudi Arabia, among others.

For each tile, we extracted 100 time series composed of 12 images of size 512 x 512 x 4 and saved them in one tfrecord file. Therefore, the training dataset is composed of 42 tfrecord files which will be available in a [Google Cloud Storage bucket](https://cloud.google.com/storage/docs/key-terms#buckets) on Monday March 4th.

The bucket address is `gs://hackathon-isae-2019/`. **In order to have access to the bucket please send me an email providing the Google account email you use for the Hackathon.**

Since 

[tf.data.Dataset object](https://www.tensorflow.org/guide/datasets)

# Code

# Submission
