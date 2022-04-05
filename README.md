# Hyperscanning2-preprocessing-eyeTracker
Processing raw eye tracker data that was recorded from HTC Vive pro eye
Particularly, chunking data based on marker and combining eye tracker data for either right-left or left-right hand for both pre-training and post-training conditions.

## Setup
<ul>
  <li> pandas >=1.2.5 </li>
  <li> numpy >=1.21.0 </li>
  <li> tqdm >=4.61.1 (if higher version doesn't work, just use this version) </li>
</ul>


## Workflow of preprocessing

### Description of  marker in recorded file (csv file)

Raw file (*.csv) that was obtained from HTC Vive pro contains all data throughout experiment. <br />

For each eye condition (i.e., averted, direct, and natural), each participant used his/her hand for 6 times, including pointing and moving. <br />
Each marker always goes in pair, it means that it has opening and closing marker; to indicate when the marker begins and ends.  <br />
Therefore, in total, there are **36 markers** =**6** (hand movement) x **3** (experimental conditions x **2** (opening & closing)  <br />

The marker is located at the column of TimeStampe which is indicated by **BEGIN1** (opening marker) and **END1** (closing marker) 

## Usage
**Step 1** : We need to extract data for every condition (each marker) and save it.....

**Step 2** : We need combine two files for each condition of pre and post. For example, odd subject (e.g., S1, S3,..etc) used to start with **right-left** hand while even subject (e.g., S2, S4,..etc) with **left-right** hand. After we run Step 1, the data for each hand is separated. Due to that, we need to combine those two files. For instance, for pre-training condition of S1, we need to combine file of **right** hand file and **left** hand file. Make sure the order is correct. Similarly, for pre-training condition of S2, we need to combine file of **left** and file and **right** hand file. Make sure the order is correct. <br >

In order to carry out such file combination, we need to run file of [extract_eye_tracker.py](extract_eye_tracker.py). <br >




