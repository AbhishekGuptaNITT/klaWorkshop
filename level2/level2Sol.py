import json
import csv
import os
import cv2

def get_image(ind):
    path = '../../dataset/level_2_data/wafer_image_' + str(ind) + '.png'
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

def in_Care_area_not_exclu(x,y):
    a = (x<=564 and x>=126) and (y>=580 and y<=874)
    b = (x<=1092 and x>=762) and (y>=490 and y<=826)
    c = (x<=807 and x>=315) and (y>=145 and y<=400)
    
    d = not (((x<=450 and x>=363) and (y>=697 and y<=790)) or ((x<=564 and x>=405) and (y>=253 and y<=313)) or ((x<=1020 and x>=900) and (y>=580 and y<=736)))
    return (a or b or c) and d

def ideal_die(images):
    my_ideal_die = []
    for i in range(1000):
        row = []
        for j in range(1200):
            value = []
            for image in images:
                value.append(image[i][j])
            row.append(max(set(value), key = value.count))
        my_ideal_die.append(row)
    return my_ideal_die

def check(my_ideal_die,images):
    # count = [1,2,3,4,5,10,9,8,7,6,11,12,13,14,15]
    count=0
    output = []
    dieno = 0
    for image in images:
        dieno +=1
        # d+=1
        for i in range(1000):
            for j in range(1200):
                if image[i][j] != int(my_ideal_die[i][j]):
                    if in_Care_area_not_exclu(j,999-i):
                        output.append([dieno,j,999-i])
    return output

def gen_csv(data):
    with open('level2Sol.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in data:
            writer.writerow([i[0],i[1],i[2]])
# print(in_Care_area_not_exclu(127,590))
images = get_images(15)
my_ideal_die = ideal_die(images)
# print(len(images),len(images[0]),len(images[0][0]))
defects = check(my_ideal_die,images)
# print(len(my_ideal_die),len(my_ideal_die[0]))
gen_csv(defects)
# print(defects)