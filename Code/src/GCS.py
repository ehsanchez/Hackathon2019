"""
This code provides some Google Cloud Storage (GCS) functions.
It requires the installation of gsutil
"""
import os


def execute(list_commands):
    """
    Executes the command line provided in list format

    :param list_commands: (list) List of commands in string format
    """
    command = " ".join(list_commands)
    os.system(command)

    return


def get_data_from_bucket(bucket, directory):
    """
    Recovers data from a given bucket

    :param directory: (string) Directory path to save the data
    :param bucket: (string) Bucket containing the data
    """
    print('\nRecovering dataset\n')
    return execute(["gsutil", "-m", "cp", "-r", bucket, directory])


def get_bucket_list(bucket):
    """
    Returns a list of the data contained in bucket

    :param bucket: (string) Bucket containing the data
    """
    print('\nBucket list\n')
    return execute(["gsutil", "ls", bucket])