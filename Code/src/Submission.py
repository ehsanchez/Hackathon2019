import pandas as pd


def to_str(int_tuple):
    """
    Perform string casting

    :param int_tuple: (Tuple of 3 ints) Location of the patch

    :return: A string containing the location of the patch
    """
    string = str(int_tuple[0])+' '+str(int_tuple[1])+' '+str(int_tuple[2])

    return string


def make_dataframe(patch_list, location_list):
    """
    Prepare the submission file by providing the patch ID and location lists

    :param patch_list: (List of int) The list containing the patch IDs. Example: [0, 1, 2, 3, 4 ...]
    :param location_list: (List of tuple of ints) The list containinf the patch location. Example: [(1,200,300), (2,412,124) ...]

    :return: A pandas.DataFrame object containing the submission information
    """

    str_patch_list = [str(patch_id) for patch_id in patch_list]
    str_location_list = [to_str(location) for location in location_list]
    submission = pd.DataFrame(columns=['Patch ID', 'Result'])

    submission['Patch ID'] = str_patch_list
    submission['Result'] = str_location_list

    return submission


def make_submission(patch_list, location_list, submission_path):
    """

    :param patch_list: (List of int) The list containing the patch IDs. Example: [0, 1, 2, 3, 4 ...]
    :param location_list: (List of tuple of ints) The list containinf the patch location. Example: [(1,200,300), (2,412,124) ...]
    :param submission_path: Path of the CSV file. Example: '/home/eduardo.sanchez/test.csv'

    :return:
    """
    submission = make_dataframe(patch_list, location_list)
    submission.to_csv(submission_path, index=False, header=True)
