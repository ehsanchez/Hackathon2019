from Code.src.Submission import make_submission
import numpy as np


# Get list of patch ID and list of locations (fake lists):
patch_list = np.arange(10)
location_list = [(np.random.randint(low=0, high=600), np.random.randint(low=0, high=448), np.random.randint(low=0, high=448)) for i in range(10)]

# Select a file name
submission_path = '~/test_submission.csv'

# Create submission!
make_submission(patch_list, location_list, submission_path)