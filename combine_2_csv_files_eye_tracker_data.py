# %% Import modules
from tqdm import tqdm
import os
from os import listdir
from os.path import isfile, join
import pandas as pd

# %% markdown
# IMPORTANT !!
# Before you begin, please look for # TODO (there are 2 places).
# Please change accordingly
# %%  Define where separated data available
# NOTE: Adjust this accordingly
path_eye_data_separated = '/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_separated'

# NOTE: Adjust this accordingly
# Define where to save combined data
path_eye_data_combined = '/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_combined'
# Get all available file names of eye tracker data that are still separated
onlyfiles = [f for f in listdir(path_eye_data_separated) if isfile(
    join(path_eye_data_separated, f))]

# %%Populate all files which have the same subject no into one list.
list_subj_files = []
file = onlyfiles[0]

for i in range(1, 33):  # TODO: : Adjust this later on according to how many subjects, eg.32
    start_idx_subj = file.find("S")
    end_idx_subj = file.index("-")
    subj_no = "S" + str(i)

    # Populate all files which have the same subject no into one list.
    subj_files = [
        idx for idx in onlyfiles if idx[start_idx_subj:end_idx_subj] == subj_no]
    list_subj_files.append(subj_files)

# %% Put all files that have the same subject no. (Pre & Post ONLY) into the same list
# Even - Pre
averted_pre_right_even = []
averted_pre_left_even = []
direct_pre_right_even = []
direct_pre_left_even = []
natural_pre_right_even = []
natural_pre_left_even = []

# Even - Post
averted_post_right_even = []
averted_post_left_even = []
direct_post_right_even = []
direct_post_left_even = []
natural_post_right_even = []
natural_post_left_even = []

# Odd - Pre
averted_pre_right_odd = []
averted_pre_left_odd = []
direct_pre_right_odd = []
direct_pre_left_odd = []
natural_pre_right_odd = []
natural_pre_left_odd = []

# Odd - Post
averted_post_right_odd = []
averted_post_left_odd = []
direct_post_right_odd = []
direct_post_left_odd = []
natural_post_right_odd = []
natural_post_left_odd = []


for idx, file in enumerate(list_subj_files):
    for idx_inside, file_inside in enumerate(file):
        start_idx_subj = file_inside.find("S")
        end_idx_subj = file_inside.index("-")
        subj_no = file_inside[start_idx_subj + 1:end_idx_subj]

        # Even subject
        if int(subj_no) % 2 == 0:
            subj = file[start_idx_subj:end_idx_subj]

            # Pre
            key_averted_pre_right_even = file_inside[0] + \
                subj_no + '-averted_pre_right'
            key_averted_pre_left_even = file_inside[0] + \
                subj_no + '-averted_pre_left'
            key_direct_pre_right_even = file_inside[0] + \
                subj_no + '-direct_pre_right'
            key_direct_pre_left_even = file_inside[0] + \
                subj_no + '-direct_pre_left'
            key_natural_pre_right_even = file_inside[0] + \
                subj_no + '-natural_pre_right'
            key_natural_pre_left_even = file_inside[0] + \
                subj_no + '-natural_pre_left'
            # Post
            key_averted_post_right_even = file_inside[0] + \
                subj_no + '-averted_post_right'
            key_averted_post_left_even = file_inside[0] + \
                subj_no + '-averted_post_left'
            key_direct_post_right_even = file_inside[0] + \
                subj_no + '-direct_post_right'
            key_direct_post_left_even = file_inside[0] + \
                subj_no + '-direct_post_left'
            key_natural_post_right_even = file_inside[0] + \
                subj_no + '-natural_post_right'
            key_natural_post_left_even = file_inside[0] + \
                subj_no + '-natural_post_left'

            # Pre-training
            if key_averted_pre_right_even in file_inside:
                averted_pre_right_even.append(
                    key_averted_pre_right_even + "_point.csv")
            elif key_averted_pre_left_even in file_inside:
                averted_pre_left_even.append(
                    key_averted_pre_left_even + "_point.csv")
            elif key_direct_pre_right_even in file_inside:
                direct_pre_right_even.append(
                    key_direct_pre_right_even + "_point.csv")
            elif key_direct_pre_left_even in file_inside:
                direct_pre_left_even.append(
                    key_direct_pre_left_even + "_point.csv")
            elif key_natural_pre_right_even in file_inside:
                natural_pre_right_even.append(
                    key_natural_pre_right_even + "_point.csv")
            elif key_natural_pre_left_even in file_inside:
                natural_pre_left_even.append(
                    key_natural_pre_left_even + "_point.csv")

            # Post-training
            elif key_averted_post_right_even in file_inside:
                averted_post_right_even.append(
                    key_averted_post_right_even + "_point.csv")
            elif key_averted_post_left_even in file_inside:
                averted_post_left_even.append(
                    key_averted_post_left_even + "_point.csv")
            elif key_direct_post_right_even in file_inside:
                direct_post_right_even.append(
                    key_direct_post_right_even + "_point.csv")
            elif key_direct_post_left_even in file_inside:
                direct_post_left_even.append(
                    key_direct_post_left_even + "_point.csv")
            elif key_natural_post_right_even in file_inside:
                natural_post_right_even.append(
                    key_natural_post_right_even + "_point.csv")
            elif key_natural_post_left_even in file_inside:
                natural_post_left_even.append(
                    key_natural_post_left_even + "_point.csv")

        # Odd subject
        else:
            subj = file[start_idx_subj:end_idx_subj]
            # Pre
            key_averted_pre_right_odd = file_inside[0] + \
                subj_no + '-averted_pre_right'
            key_averted_pre_left_odd = file_inside[0] + \
                subj_no + '-averted_pre_left'
            key_direct_pre_right_odd = file_inside[0] + \
                subj_no + '-direct_pre_right'
            key_direct_pre_left_odd = file_inside[0] + \
                subj_no + '-direct_pre_left'
            key_natural_pre_right_odd = file_inside[0] + \
                subj_no + '-natural_pre_right'
            key_natural_pre_left_odd = file_inside[0] + \
                subj_no + '-natural_pre_left'

            # Post
            key_averted_post_right_odd = file_inside[0] + \
                subj_no + '-averted_post_right'
            key_averted_post_left_odd = file_inside[0] + \
                subj_no + '-averted_post_left'
            key_direct_post_right_odd = file_inside[0] + \
                subj_no + '-direct_post_right'
            key_direct_post_left_odd = file_inside[0] + \
                subj_no + '-direct_post_left'
            key_natural_post_right_odd = file_inside[0] + \
                subj_no + '-natural_post_right'
            key_natural_post_left_odd = file_inside[0] + \
                subj_no + '-natural_post_left'

            # Pre-training
            if key_averted_pre_right_odd in file_inside:
                averted_pre_right_odd.append(
                    key_averted_pre_right_odd + "_point.csv")
            elif key_averted_pre_left_odd in file_inside:
                averted_pre_left_odd.append(
                    key_averted_pre_left_odd + "_point.csv")
            elif key_direct_pre_right_odd in file_inside:
                direct_pre_right_odd.append(
                    key_direct_pre_right_odd + "_point.csv")
            elif key_direct_pre_left_odd in file_inside:
                direct_pre_left_odd.append(
                    key_direct_pre_left_odd + "_point.csv")
            elif key_natural_pre_right_odd in file_inside:
                natural_pre_right_odd.append(
                    key_natural_pre_right_odd + "_point.csv")
            elif key_natural_pre_left_odd in file_inside:
                natural_pre_left_odd.append(
                    key_natural_pre_left_odd + "_point.csv")

            # Post-training
            elif key_averted_post_right_odd in file_inside:
                averted_post_right_odd.append(
                    key_averted_post_right_odd + "_point.csv")
            elif key_averted_post_left_odd in file_inside:
                averted_post_left_odd.append(
                    key_averted_post_left_odd + "_point.csv")
            elif key_direct_post_right_odd in file_inside:
                direct_post_right_odd.append(
                    key_direct_post_right_odd + "_point.csv")
            elif key_direct_post_left_odd in file_inside:
                direct_post_left_odd.append(
                    key_direct_post_left_odd + "_point.csv")
            elif key_natural_post_right_odd in file_inside:
                natural_post_right_odd.append(
                    key_natural_post_right_odd + "_point.csv")
            elif key_natural_post_left_odd in file_inside:
                natural_post_left_odd.append(
                    key_natural_post_left_odd + "_point.csv")


# %% Combine list for left-right (even) and right-left(odd)
# TODO: Adjust the value of range according to how many files to combine in a list,
# eg. find len(averted_pre_left_even) = 16  or len(averted_pre_right_even) = 16

for idx in tqdm(range(16), desc="In progress Bro...:)"): 

    # ####################### Even subject and Pre-training ##################

    # Averted pre combined even
    df1_averted_pre_even = pd.read_csv(os.path.join(
        path_eye_data_separated, averted_pre_left_even[idx]))  # Left
    df2_averted_pre_even = pd.read_csv(os.path.join(
        path_eye_data_separated, averted_pre_right_even[idx]))  # Right
    df_combined_averted_pre_even = pd.concat(
        [df1_averted_pre_even, df2_averted_pre_even], ignore_index=True)
    # save to csv file
    # NOTE: this is even subject from 2, 4, etc ...
    fname_combined_averted_pre_even = "S" + \
        str(idx * 2 + 2) + "-averted_pre_" + "left_right_combined" + ".csv"
    df_combined_averted_pre_even.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_averted_pre_even))

    # Direct pre combined even
    df1_direct_pre_even = pd.read_csv(os.path.join(
        path_eye_data_separated, direct_pre_left_even[idx]))  # Left
    df2_direct_pre_even = pd.read_csv(os.path.join(
        path_eye_data_separated, direct_pre_right_even[idx]))  # Right
    df_combined_direct_pre_even = pd.concat(
        [df1_direct_pre_even, df2_direct_pre_even], ignore_index=True)
    # save to csv file
    # NOTE: this is even subject from 2, 4, etc ...
    fname_combined_direct_pre_even = "S" + \
        str(idx * 2 + 2) + "-direct_pre_" + "left_right_combined" + ".csv"
    df_combined_direct_pre_even.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_direct_pre_even))

    # Natural pre combined even
    df1_natural_pre_even = pd.read_csv(os.path.join(
        path_eye_data_separated, natural_pre_left_even[idx]))  # Left
    df2_natural_pre_even = pd.read_csv(os.path.join(
        path_eye_data_separated, natural_pre_right_even[idx]))  # Right
    df_combined_natural_pre_even = pd.concat(
        [df1_natural_pre_even, df2_natural_pre_even], ignore_index=True)
    # save to csv file
    # NOTE: this is even subject from 2, 4, etc ...
    fname_combined_natural_pre_even = "S" + \
        str(idx * 2 + 2) + "-natural_pre_" + "left_right_combined" + ".csv"
    df_combined_natural_pre_even.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_natural_pre_even))

    # ####################### Even subject and Post-training ##################

    # Averted post combined even
    df1_averted_post_even = pd.read_csv(os.path.join(
        path_eye_data_separated, averted_post_left_even[idx]))  # Left
    df2_averted_post_even = pd.read_csv(os.path.join(
        path_eye_data_separated, averted_post_right_even[idx]))  # Right
    df_combined_averted_post_even = pd.concat(
        [df1_averted_post_even, df2_averted_post_even], ignore_index=True)
    # save to csv file
    # NOTE: this is even subject from 2, 4, etc ...
    fname_combined_averted_post_even = "S" + \
        str(idx * 2 + 2) + "-averted_post_" + "left_right_combined" + ".csv"
    df_combined_averted_post_even.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_averted_post_even))

    # Direct post combined even
    df1_direct_post_even = pd.read_csv(os.path.join(
        path_eye_data_separated, direct_post_left_even[idx]))  # Left
    df2_direct_post_even = pd.read_csv(os.path.join(
        path_eye_data_separated, direct_post_right_even[idx]))  # Right
    df_combined_direct_post_even = pd.concat(
        [df1_direct_post_even, df2_direct_post_even], ignore_index=True)
    # save to csv file
    # NOTE: this is even subject from 2, 4, etc ...
    fname_combined_direct_post_even = "S" + \
        str(idx * 2 + 2) + "-direct_post_" + "left_right_combined" + ".csv"
    df_combined_direct_post_even.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_direct_post_even))

    # Natural post combined even
    df1_natural_post_even = pd.read_csv(os.path.join(
        path_eye_data_separated, natural_post_left_even[idx]))  # Left
    df2_natural_post_even = pd.read_csv(os.path.join(
        path_eye_data_separated, natural_post_right_even[idx]))  # Right
    df_combined_natural_post_even = pd.concat(
        [df1_natural_post_even, df2_natural_post_even], ignore_index=True)
    # save to csv file
    # NOTE: this is even subject from 2, 4, etc ...
    fname_combined_natural_post_even = "S" + \
        str(idx * 2 + 2) + "-natural_post_" + "left_right_combined" + ".csv"
    df_combined_natural_post_even.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_natural_post_even))

    # ####################### Odd subject and Pre-training ##################

    # Averted pre combined odd
    df1_averted_pre_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, averted_pre_right_odd[idx]))  # Right
    df2_averted_pre_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, averted_pre_left_odd[idx]))  # Left
    df_combined_averted_pre_odd = pd.concat(
        [df1_averted_pre_odd, df2_averted_pre_odd], ignore_index=True)
    # save to csv file
    # NOTE: this is odd subject from 1, 3, etc ...
    fname_combined_averted_pre_odd = "S" + \
        str(idx * 2 + 1) + "-averted_pre_" + "right_left_combined" + ".csv"
    df_combined_averted_pre_odd.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_averted_pre_odd))

    # Direct pre combined odd
    df1_direct_pre_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, direct_pre_right_odd[idx]))  # Right
    df2_direct_pre_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, direct_pre_left_odd[idx]))  # Left
    df_combined_direct_pre_odd = pd.concat(
        [df1_direct_pre_odd, df2_direct_pre_odd], ignore_index=True)
    # save to csv file
    # NOTE: this is odd subject from 1, 3, etc ...
    fname_combined_direct_pre_odd = "S" + \
        str(idx * 2 + 1) + "-direct_pre_" + "right_left_combined" + ".csv"
    df_combined_direct_pre_odd.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_direct_pre_odd))

    # Natural pre combined odd
    df1_natural_pre_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, natural_pre_right_odd[idx]))  # Right
    df2_natural_pre_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, natural_pre_left_odd[idx]))  # Left
    df_combined_natural_pre_odd = pd.concat(
        [df1_natural_pre_odd, df2_natural_pre_odd], ignore_index=True)
    # save to csv file
    # NOTE: this is odd subject from 1, 3, etc ...
    fname_combined_natural_pre_odd = "S" + \
        str(idx * 2 + 1) + "-natural_pre_" + "right_left_combined" + ".csv"
    df_combined_natural_pre_odd.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_natural_pre_odd))

    # ####################### Odd subject and Post-training ##################

    # Averted post combined odd
    df1_averted_post_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, averted_post_right_odd[idx]))  # Right
    df2_averted_post_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, averted_post_left_odd[idx]))  # Left
    df_combined_averted_post_odd = pd.concat(
        [df1_averted_post_odd, df2_averted_post_odd], ignore_index=True)
    # save to csv file
    # NOTE: this is odd subject from 1, 3, etc ...
    fname_combined_averted_post_odd = "S" + \
        str(idx * 2 + 1) + "-averted_post_" + "right_left_combined" + ".csv"
    df_combined_averted_post_odd.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_averted_post_odd))

    # Direct post combined odd
    df1_direct_post_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, direct_post_right_odd[idx]))  # Right
    df2_direct_post_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, direct_post_left_odd[idx]))  # Left
    df_combined_direct_post_odd = pd.concat(
        [df1_direct_post_odd, df2_direct_post_odd], ignore_index=True)
    # save to csv file
    # NOTE: this is odd subject from 1, 3, etc ...
    fname_combined_direct_post_odd = "S" + \
        str(idx * 2 + 1) + "-direct_post_" + "right_left_combined" + ".csv"
    df_combined_direct_post_odd.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_direct_post_odd))

    # Natural post combined odd
    df1_natural_post_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, natural_post_right_odd[idx]))  # Right
    df2_natural_post_odd = pd.read_csv(os.path.join(
        path_eye_data_separated, natural_post_left_odd[idx]))  # Left
    df_combined_natural_post_odd = pd.concat(
        [df1_natural_post_odd, df2_natural_post_odd], ignore_index=True)
    # save to csv file
    # NOTE: this is odd subject from 1, 3, etc ...
    fname_combined_natural_post_odd = "S" + \
        str(idx * 2 + 1) + "-natural_post_" + "right_left_combined" + ".csv"
    df_combined_natural_post_odd.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_natural_post_odd))
print("All eye tracker files have been combined. Done ! ")
