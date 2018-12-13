#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

#print '参数个数为:', len(sys.argv), '个参数。'
#print '参数列表:', str(sys.argv)

#test_txt = 'images_result'

test_txt = sys.argv[1]
print test_txt

def load_label_set(label_dir):
    losses = 0
    count = 0
    label_folder = open(label_dir, "r")
    trainlines = label_folder.read().splitlines()  #返回每一行的数据
    for line in trainlines:
        line = line.split(" ")  #按照空格键分割每一行里面的数据
        count += 1
	#print 'count=', count

        box = [int(line[0]), int(line[1])]#box读取标签ground_truth
	loss = box[1] - box[0]
	print loss
        #if 0 != int(line[0]):
	    #loss = float(box[1] - box[0])/ float(line[0])
	    #print box[1]
	    #print box[0]
            #losses += abs(loss)

    #print losses
    label_folder.close()

#return  train_box

load_label_set(test_txt)
