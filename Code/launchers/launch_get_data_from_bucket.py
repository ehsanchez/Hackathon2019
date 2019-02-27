import Code.src.GCS as GCS


bucket = "gs://hackathon-isae-2019/"

# Check the content of the bucket
GCS.get_bucket_list(bucket=bucket)

# Download the bucket and save in a directory
directory = '~/Data'
GCS.get_data_from_bucket(bucket=bucket, directory=directory)