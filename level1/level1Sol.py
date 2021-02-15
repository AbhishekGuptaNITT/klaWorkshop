import csv
import os
import cv2

def get_image(ind):
    path = '../../dataset/level_1_data/wafer_image_' + str(ind) + '.png'
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print(image)
    return image

def get_images(num_images):
    images = []
    for i in range(num_images):
        images.append(get_image(i+1))
    # print(len(images),len(images[0]))
    return images

def ideal_die(images):
    my_ideal_die = []
    for i in range(600):
        row = []
        for j in range(800):
            value = []
            for image in images:
                value.append(image[i][j])
            row.append(max(set(value), key = value.count))
        my_ideal_die.append(row)
    return my_ideal_die

def check(my_ideal_die,images):
    count = 0
    output = []
    for image in images:
        count+=1
        for i in range(600):
            for j in range(800):
                if image[i][j] != int(my_ideal_die[i][j]):
                    output.append([count,j,599-i])
    return output

def gen_csv(data):
    with open('level1Sol.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in data:
            writer.writerow([i[0],i[1],i[2]])

images = get_images(5)
my_ideal_die = ideal_die(images)
defects = check(my_ideal_die,images)
# print(len(my_ideal_die),len(my_ideal_die[0]))
gen_csv(defects)
# print(defects)
