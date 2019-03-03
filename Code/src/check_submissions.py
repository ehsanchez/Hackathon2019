import pandas
import numpy as np


def to_int_tuple(result):
    int_tuple = tuple(result.split(' '))
    int_tuple = (int(int_tuple[0]), int(int_tuple[1]), int(int_tuple[2]))
    return int_tuple


def sort_submission_lists(patch_list, location_list):
    length = len(patch_list)
    index = sorted(range(length), key=lambda k: patch_list[k])

    new_patch_list = []
    new_location_list = []

    for i in range(length):
        new_patch_list.append(patch_list[index[i]])
        new_location_list.append(location_list[index[i]])

    return new_patch_list, new_location_list


def get_csv_lists(dataframe):
    patch_list = dataframe['Patch ID'].tolist()
    location_list = dataframe['Result'].tolist()
    assert len(patch_list) == 38400
    assert len(patch_list) == len(location_list)
    patch_list, location_list = sort_submission_lists(patch_list, location_list)
    new_location_list = [to_int_tuple(result) for result in location_list]

    return patch_list, new_location_list


def compare(result, answer):
    score = 0
    if result[0] == answer[0]:
        score += 0.5
        distance = 1 - (np.sqrt((result[1] - answer[1])**2 + (result[2] - answer[2])**2)/np.sqrt(64**2 + 64**2))
        score += 0.5 * np.maximum(distance, 0.0)
        return score
    else:
        return score


def get_score(sbm_location_list, aws_location_list):
    score = 0
    length = len(sbm_location_list)
    for result, answer in zip(sbm_location_list, aws_location_list):
        score += compare(result, answer)
    return score/length


def get_submission_score(submission, answers):
    submission_pd = pandas.read_csv(submission)
    answers_pd = pandas.read_csv(answers)
    sbm_patch_list, sbm_location_list = get_csv_lists(submission_pd)
    aws_patch_list, aws_location_list = get_csv_lists(answers_pd)

    assert len(sbm_patch_list) == len(aws_patch_list)
    score = get_score(sbm_location_list, aws_location_list)

    return score
