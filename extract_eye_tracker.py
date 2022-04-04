import os
import mne
import pandas as pd
# from progressbar import progressbar
from tqdm import tqdm

def extract_eye_data(filename: str , labelsequence: int) :
    try:
        f = open(filename)
        labelsequence = int(labelsequence)

    except IOError as err_filename:
        print("The format of file name is not correct or file doesn't exist \nThe format must be 'EyeTracker-Sx.csv' , x=subject number ")
        raise
    except ValueError as err_integer:
        print("The labelsequence input must be integer : ", err_integer)
        raise

    else:
        if labelsequence < 1 or labelsequence > 12:
            print(
                "The value for labelsequence parameter is out of range. It must be be between 1 and 12")
            raise IndexError
    # else:


        # %% Load the data
        original_data_path = "/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_original/" # TODO: Adjust this in case using for other experimental data
        # filename = "EyeTracker-S1.csv"
        path_filename = os.path.join(original_data_path, filename)
        # print(filename)
        # %%
        # filename = "EyeTracker-S1.csv"
        fileName = filename  # The format of file name of Eye Tracker file must be like this
        print("Processing file : " + fileName)
        df = pd.read_csv(path_filename, delimiter=',')
        # df.head()

        # %% replace all markers of "BEGIN*" and "END*" with 9999999
        df['UnixTimeStamp'] = df.UnixTimeStamp.apply(
            lambda x: '9999999' if 'BEGIN' in x else x)
        df['UnixTimeStamp'] = df.UnixTimeStamp.apply(
            lambda x: '9999999' if 'END' in x else x)

        # Turn the UnixTimeStamp column into a list (we need the marker later on)
        markers = df['UnixTimeStamp'].tolist()
        # %%  Find all experimental markers and print them out.

        indicesOfMarkers = []  # Empty list to contain indices of markers
        for i, c in enumerate(markers):
            if "9999999" in str(c):
                indicesOfMarkers.append(i)  # check if the number of markers = 36
        try:
            number_markers = len(indicesOfMarkers)
            if number_markers != 36:  # The number of markers have to be 36
                raise ValueError("The {} file has incorrect number of markers : {} ! It MUST be 36".format(
                    fileName, number_markers))
        except ValueError as err_unmatch_markers:
            print(err_unmatch_markers)
            raise

        # %% Loop the list of labels in sequence
        # todo Create a list of labels with different sequences and put them into a list (list of list)

        # Order = 1 (Averted/Direct/Natural)
        oddOrder1 = ["averted_pre_right_point", "averted_pre_left_point", "averted_left_tracking", "averted_right_tracking",
                     "averted_post_right_point", "averted_post_left_point", "direct_pre_right_point", "direct_pre_left_point",
                     "direct_left_tracking", "direct_right_tracking", "direct_post_right_point", "direct_post_left_point",
                     "natural_pre_right_point", "natural_pre_left_point", "natural_left_tracking", "natural_right_tracking",
                     "natural_post_right_point", "natural_post_left_point"]

        evenOrder1 = ["averted_pre_left_point", "averted_pre_right_point", "averted_right_tracking", "averted_left_tracking",
                      "averted_post_left_point", "averted_post_right_point", "direct_pre_left_point", "direct_pre_right_point",
                      "direct_right_tracking", "direct_left_tracking", "direct_post_left_point", "direct_post_right_point",
                      "natural_pre_left_point", "natural_pre_right_point", "natural_right_tracking", "natural_left_tracking",
                      "natural_post_left_point", "natural_post_right_point"]

        # Order = 2 (Averted/Natural/Direct)
        oddOrder2 = ["averted_pre_right_point", "averted_pre_left_point", "averted_left_tracking", "averted_right_tracking",
                     "averted_post_right_point", "averted_post_left_point", "natural_pre_right_point", "natural_pre_left_point",
                     "natural_left_tracking", "natural_right_tracking", "natural_post_right_point", "natural_post_left_point",
                     "direct_pre_right_point", "direct_pre_left_point", "direct_left_tracking", "direct_right_tracking",
                     "direct_post_right_point", "direct_post_left_point"]

        evenOrder2 = ["averted_pre_left_point", "averted_pre_right_point", "averted_right_tracking", "averted_left_tracking",
                      "averted_post_left_point", "averted_post_right_point", "natural_pre_left_point", "natural_pre_right_point",
                      "natural_right_tracking", "natural_left_tracking", "natural_post_left_point", "natural_post_right_point",
                      "direct_pre_left_point", "direct_pre_right_point", "direct_right_tracking", "direct_left_tracking",
                      "direct_post_left_point", "direct_post_right_point"]

        # Order = 3 (Direct / Natural / Averted)
        oddOrder3 = ["direct_pre_right_point", "direct_pre_left_point", "direct_left_tracking", "direct_right_tracking",
                     "direct_post_right_point", "direct_post_left_point", "natural_pre_right_point", "natural_pre_left_point",
                     "natural_left_tracking", "natural_right_tracking", "natural_post_right_point", "natural_post_left_point",
                     "averted_pre_right_point", "averted_pre_left_point", "averted_left_tracking", "averted_right_tracking",
                     "averted_post_right_point", "averted_post_left_point"]

        evenOrder3 = ["direct_pre_left_point", "direct_pre_right_point", "direct_right_tracking", "direct_left_tracking",
                      "direct_post_left_point", "direct_post_right_point", "natural_pre_left_point", "natural_pre_right_point",
                      "natural_right_tracking", "natural_left_tracking", "natural_post_left_point", "natural_post_right_point",
                      "averted_pre_left_point", "averted_pre_right_point", "averted_right_tracking", "averted_left_tracking",
                      "averted_post_left_point", "averted_post_right_point"]

        # Order = 4 (Direct/Averted/Natural)
        oddOrder4 = ["direct_pre_right_point", "direct_pre_left_point", "direct_left_tracking", "direct_right_tracking",
                     "direct_post_right_point", "direct_post_left_point", "averted_pre_right_point", "averted_pre_left_point",
                     "averted_left_tracking", "averted_right_tracking", "averted_post_right_point", "averted_post_left_point",
                     "natural_pre_right_point", "natural_pre_left_point", "natural_left_tracking", "natural_right_tracking",
                     "natural_post_right_point", "natural_post_left_point"]

        evenOrder4 = ["direct_pre_left_point", "direct_pre_right_point", "direct_right_tracking", "direct_left_tracking",
                      "direct_post_left_point", "direct_post_right_point", "averted_pre_left_point", "averted_pre_right_point",
                      "averted_right_tracking", "averted_left_tracking", "averted_post_left_point", "averted_post_right_point",
                      "natural_pre_left_point", "natural_pre_right_point", "natural_right_tracking", "natural_left_tracking",
                      "natural_post_left_point", "natural_post_right_point"]

        # Order = 5 (Natural/Direct/Averted)
        oddOrder5 = ["natural_pre_right_point", "natural_pre_left_point", "natural_left_tracking", "natural_right_tracking",
                     "natural_post_right_point", "natural_post_left_point", "direct_pre_right_point", "direct_pre_left_point",
                     "direct_left_tracking", "direct_right_tracking", "direct_post_right_point", "direct_post_left_point",
                     "averted_pre_right_point", "averted_pre_left_point", "averted_left_tracking", "averted_right_tracking",
                     "averted_post_right_point", "averted_post_left_point"]

        evenOrder5 = ["natural_pre_left_point", "natural_pre_right_point", "natural_right_tracking", "natural_left_tracking",
                      "natural_post_left_point", "natural_post_right_point", "direct_pre_left_point", "direct_pre_right_point",
                      "direct_right_tracking", "direct_left_tracking", "direct_post_left_point", "direct_post_right_point",
                      "averted_pre_left_point", "averted_pre_right_point", "averted_right_tracking", "averted_left_tracking",
                      "averted_post_left_point", "averted_post_right_point"]

        # Order = 6 (Natural/Averted/Direct)
        oddOrder6 = ["natural_pre_right_point", "natural_pre_left_point", "natural_left_tracking", "natural_right_tracking",
                     "natural_post_right_point", "natural_post_left_point", "averted_pre_right_point", "averted_pre_left_point",
                     "averted_left_tracking", "averted_right_tracking", "averted_post_right_point", "averted_post_left_point",
                     "direct_pre_right_point", "direct_pre_left_point", "direct_left_tracking", "direct_right_tracking",
                     "direct_post_right_point", "direct_post_left_point"]

        evenOrder6 = ["natural_pre_left_point", "natural_pre_right_point", "natural_right_tracking", "natural_left_tracking",
                      "natural_post_left_point", "natural_post_right_point", "averted_pre_left_point", "averted_pre_right_point",
                      "averted_right_tracking", "averted_left_tracking", "averted_post_left_point", "averted_post_right_point",
                      "direct_pre_left_point", "direct_pre_right_point", "direct_right_tracking", "direct_left_tracking",
                      "direct_post_left_point", "direct_post_right_point"]
        # %% Add all labels into a list

        listOfOrders = []

        for i in tqdm(range(6)):
            # Append odd order labels
            listOfOrders.append(eval('oddOrder' + str(i + 1)))
            # Append even order labels
            listOfOrders.append(eval('evenOrder' + str(i + 1)))

        # TODO:  !  VERY IMPORTANT !!!
        # chosenOrder = listOfOrders[labelsequence-1] # Uncomment this later when the function works

        # TODO: !  VERY IMPORTANT !!!
        # Comment this  when the above line is uncommented
        chosenOrder = listOfOrders[0]

        # %% Chunk the data based on opening and closing markers
        chunkedData = []
        for i in range(0, 36, 2):
            chunkedData.append(
                df.iloc[indicesOfMarkers[i]: indicesOfMarkers[i + 1] + 1, 1:22])

        # %% Save the chunkedData into a separate csv file
        path = "/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_separated/"
        for idx, label in enumerate(chosenOrder):
            char_idx = filename.find("-")
            sub_no = filename[char_idx+1:filename.index(".")]
            label_fname = sub_no + "-" + chosenOrder[idx] + ".csv"
            chunkedData[idx].to_csv(os.path.join(path, label_fname))

    print("Data have been extracted from : " + fileName)
