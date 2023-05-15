# Lint as: python3
# coding=utf-8
# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Prepare data for further process.

Read data from "/slope", "/ring", "/wing", "/negative" and save them
in "/data/complete_data" in python dict format.

It will generate a new file with the following structure:
├── data
│   └── complete_data
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import json
import os
import random

LABEL_NAME = "gesture"
DATA_NAME = "accel_ms2_xyz"
# gesture_names = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]
gesture_names = ["01","03","05","09"]
sample_names = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]
people_names = ["A","B","C","D","E","F","G","H"]

def prepare_original_data(gesture_name, people_name, data, file_to_read): # folder, name
    """Read collected data from files."""
    with open(file_to_read, "r") as f:
            lines = csv.reader(f)

            data_new = {}
            data_new[LABEL_NAME] = gesture_name
            data_new[DATA_NAME] = []  
            data_new["name"] = people_name

            for idx, line in enumerate(lines):    # pylint: disable=unused-variable
                # print(line[0].split())
                line_vals = line[0].split()
                data_new[DATA_NAME].append([float(i) for i in line_vals[3:6]])

            data.append(data_new)


# Write data to file
def write_data(data_to_write, path):
    with open(path, "w") as f:
        for idx, item in enumerate(data_to_write):    # pylint: disable=unused-variable
            dic = json.dumps(item, ensure_ascii=False)
            f.write(dic)
            f.write("\n")


if __name__ == "__main__":
    data = []
    for idx1, people_name in enumerate(people_names):
        for idx2, gesture_name in enumerate(gesture_names):
            for idx3, sample_name in enumerate(sample_names):
                prepare_original_data(gesture_name, people_name, data, "./gestures-dataset/%s/%s/%s.txt" % (people_name, gesture_name, sample_name))
  
    print("data_length: " + str(len(data)))
    if not os.path.exists("./data"):
        os.makedirs("./data")
    write_data(data, "./data/complete_data")
