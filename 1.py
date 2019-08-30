import numpy as np

image=np.array([[80,80,255,80,80,255,80,80],
            [80,80,255,80,80,255,80,80],
            [255,80,120,120,120,120,255,80],
            [255,80,255,255,255,255,80,80],
            [255,80,120,120,120,120,80,80]])

#1  Lighten the image 
def lighten(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] >= 255:
                return True
            else:
                array[i][j] *= 1+0.1
    return array

print('1:',lighten(image))

#2  Flip (reflect) the image 
def flip(array):
    for i in array:
        for j in range(4):
            i[j], i[7-j] = i[7-j], i[j]
    return array

print('2:',flip(image))

#3 Clip the image
def clip(array,MaxVal):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = MaxVal
    return array

print('3:',clip(image,255))
