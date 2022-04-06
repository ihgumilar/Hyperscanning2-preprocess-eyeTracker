# Hyperscanning2-preprocessing-eyeTracker
Processing raw eye tracker data that was recorded from HTC Vive pro eye
Particularly, chunking data based on marker and combining eye tracker data for either right-left or left-right hand for both pre-training and post-training conditions.

## Setup
<ul>
  <li> pandas >=1.2.5 </li>
  <li> numpy >=1.21.0 </li>
  <li> tqdm >=4.61.1 (if higher version doesn't work, just use this version) </li>
  <li> pickle </li>
</ul>


## Workflow of preprocessing

### Description of  marker in recorded file (csv file)

Raw file (*.csv) that was obtained from HTC Vive pro contains all data throughout experiment. <br />

For each eye condition (i.e., averted, direct, and natural), each participant used his/her hand for 6 times, including pointing and moving. Each marker always goes in pair, it means that it has opening and closing marker; to indicate when the marker begins and ends. Therefore, in total, there are **36 markers** =**6** (hand movement) x **3** (experimental conditions x **2** (opening & closing).  <br />

The marker is located at the column of TimeStampe which is indicated by **BEGIN1** (opening marker) and **END1** (closing marker) 

## Usage
**Step 1** : We need to extract data for every condition (each marker) by using [extract_eye_tracker.py](extract_eye_tracker.py). <br >
It will save the data into csv file. <br >

**Step 2** : We need combine two files for each condition of pre and post. For example, odd subject (e.g., S1, S3,..etc) used to start with **right-left** hand while even subject (e.g., S2, S4,..etc) with **left-right** hand. After we run Step 1, the data for each hand is separated. Due to that, we need to combine those two files. For instance, for pre-training condition of S1, we need to combine file of **right** hand file and **left** hand file. Make sure the order is correct. Similarly, for pre-training condition of S2, we need to combine file of **left** and file and **right** hand file. Make sure the order is correct. In order to carry out such file combination, we need to run [combine_2_csv_files_eye_tracker_data.py](https://github.com/ihgumilar/Hyperscanning2-preprocess-eyeTracker/blob/main/combine_2_csv_files_eye_tracker_data.py).

**Step 3** : In this particular project (Hyperscanning2), EEG becomes a reference. If any data in EEG is removed, then similar data on the side (same timestamp) of Eye tracker data needs to be removed as well. For doing such activity, there are two steps that we need to do : <br > 
<ol>
  <li> 1. Load a pickle file which contains a list of indices of deleted EEG data. </li>
  <li> 2. Run a function of delete_epoch_eye_tracker from cleaning_eye_tracker_data.py. </li>
</ol>

Your files are ready, bro !

 




