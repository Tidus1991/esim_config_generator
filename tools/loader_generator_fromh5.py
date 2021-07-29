"""
File  : loader_generator.py
Author: Tidus
Date  : 2021/7/2
Email : jinyj9@lenovo.com
"""

import csv
import glob
import os
import argparse
import random


def write_path(path):
    files = sorted(glob.glob('{}/*.h5'.format(path)))
    data_length = len(files)
    if data_length > 1:
        train_length = int(data_length * percent * 0.01)
        random.shuffle(files)
        with open(path+"/train_list.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for i in range(0, train_length):
                print(files[i])
                writer.writerow([str(os.path.abspath(files[i]))])

        with open(path+"/val_list.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for j in range(train_length, data_length):
                print(files[j])
                writer.writerow([str(os.path.abspath(files[j]))])

        print(os.path.abspath(path) + "/train_list.csv")
        print(os.path.abspath(path) + "/val_list.csv")
        
    else:
        print("The dataset is too small")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate data_loader file from h5 folder')
    parser.add_argument('path', type=str, help='path to h5 folder')
    parser.add_argument('--train_p', type=int, default=70, help='percentage of train data')
    args = parser.parse_args()
    path = args.path
    percent = args.train_p
    assert (not os.path.isfile(path))
    write_path(path)