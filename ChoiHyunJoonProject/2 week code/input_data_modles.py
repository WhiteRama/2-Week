import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random

FLAGS = tf.app.flags.FLAGS
FLAGS.width = 28
FLAGS.height = 28
FLAGS.depth = 3
batch_index = 0
filenames = []

def get_filenames(data_set): 
    # Get file names under sub-directory.
    global filenames
    labels = []
    '''
        with open(FLAGS.data_dir + '/labels') as f:
            for line in f:
                inner_list = [elt.strip() for elt in line.split(',')]
                labels += inner_list 
                # Insert labels into List.
                # Read many line to insert labels.

        for i, label in enumerate(labels): 
            # check files in label`s directory and insert it into list.
            list = os.listdir(FLAGS.data_dir  + '/' + data_set + '/' + label)
            for filename in list:
                # Add to list file name and label`s number.
                filenames.append([label + '/' + filename, i]) 

        random.shuffle(filenames) 
    '''
    label_dir = os.listdir(FLAGS.data_dir + '/' + data_set)
    # File`s directory is data_dir + data_set( eval, train )...
    for filename in label_dir:
        filenames.append([filename, 0])
    
    # shuffle files because file must be trained with non-ordered ways.
    random.shuffle(filenames) 

def get_data_jpeg(sess, data_set, batch_size, recheck=False):
    global batch_index, filenames
    filenames=[]

    if len(filenames) == 0:
        # if file name is null, read one more time.
        get_filenames(data_set)
    if recheck:
        get_filenames(data_set)
    max = len(filenames)
    # Set range to read now index to batch_size.
    begin = batch_index
    end = batch_index + batch_size

    if end >= max:
        # if size is larger then max, set 0.
        end = max
        batch_index = 0

    x_data = np.array([])
    y_data = np.zeros((batch_size, 1))
    # For one hot encoding, make 0-filled list.
    index = 0

    for i in range(begin, end):
        # Read files...
        with tf.gfile.FastGFile(FLAGS.data_dir + '/' + data_set + '/' + filenames[i][0], 'rb') as f:
            image_data = f.read()
        
        # this is JPEG files, so decoding is needed..

        decode_image = tf.image.decode_jpeg(image_data, channels=FLAGS.depth)
        resized_image = tf.image.resize_images(decode_image, FLAGS.height, FLAGS.width, method=1) 
        image = sess.run(resized_image) 
        # run sess operation.
        # To insert String Type data to Tensorflow, change to array.
        # It must be float type nomalized with dividing 255.
        # if not, cross entropy will be nan.
        x_data = np.append(x_data, np.asarray(image.data, dtype='float32'))
        y_data[index][filenames[i][1]] = 1
        
        # Set Column 1 which labels is correct. ( one hot encoding )
        index += 1
        # for check changed image, release comment.
        # print image.shape, len(image.data)
        # im = np.reshape(image.data, (28, 28, 3))
        # plt.imshow(im)
        # plt.show()

    batch_index += batch_size 
    # for next batch, renew index.

    try:
        # Exception for broken images.
        x_data = x_data.reshape(batch_size, FLAGS.height * FLAGS.width * FLAGS.depth)
    except:
        return None, None

    return x_data, y_data