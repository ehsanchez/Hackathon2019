from Code.src.Submission import make_submission
from Code.src.check_submissions import get_submission_score
import numpy as np


# Get list of patch ID and list of locations (fake lists):
size = 38400
patch_list = np.arange(size)
location_list = [(np.random.randint(low=0, high=600), np.random.randint(low=0, high=448), np.random.randint(low=0, high=448)) for i in range(size)]

# Select a file name
submission_path = '~/test_submission.csv'
real_path = '~/real_submission.csv'

# Create submissions
make_submission(patch_list, location_list, submission_path)

location_list[0] = (location_list[0][0]+0, location_list[0][1]+4, location_list[0][2]+4)
location_list[1] = (location_list[1][0]+0, location_list[1][1]+7, location_list[1][2]+6)

make_submission(patch_list, location_list, real_path)

print('Your submission score is: %s' % get_submission_score(submission_path, real_path))