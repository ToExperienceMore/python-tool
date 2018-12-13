#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)

#test_txt = 'images_result'

test_txt = sys.argv[1]
print test_txt

def load_label_set(label):
    losses = 0
    count = 0
    count_0 = 0
    label_file = open(label, "r")
    trainlines = label_file.read().splitlines()  #返回每一行的数据

    for line in trainlines:
        line = line.split(" ")  #按照空格键分割每一行里面的数据
        count += 1
	#print 'count=', count

        box = [int(line[1]), int(line[2]), int(line[3])]#box读取标签ground_truth
        if (box[1] - box[0] != box[2]):
	    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=', count
            return

        if 0 != box[0]:
	    loss = float(box[2])/ float(box[0])
        else:
            if box[0] == 0 and box[2] != 0:
	        loss = 1
                count_0 += 1

            if box[0] == 0 and box[2] == 0:
	        loss = 0

	    #print box[1]
	    #print box[0]
	print loss
        losses += abs(loss)

    print 'count_0=', count_0
    print 'losses=', losses
    print 'count=', count
    print 'ave_loss=', losses/count

    label_file.close()

#return  train_box

load_label_set(test_txt)
