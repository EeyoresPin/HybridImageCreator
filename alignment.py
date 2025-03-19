import cv2
import numpy as np

def affineTransform(image1File, image2File, key1File, key2File):


    image1 = cv2.imread(image1File)
    image2 = cv2.imread(image2File)
    
    height, width, c = image1.shape
    height2, width2, c2 = image2.shape

    yScale  = height/ height2
    xScale = width/width2


    keypoints1 = []
    tmp1 = []

    keypoints2 = []
    tmp2 = []


    file = open(key1File, "r")
    for line in file:
        cleanLine = line.replace('\n','')
        tmp1.append(cleanLine)

    for item in tmp1:
        keypoints1.append(list(map(int, item.split(' '))))
    file.close()

    file = open(key2File, "r")
    for line in file:
        cleanLine = line.replace('\n','')
        tmp2.append(cleanLine)

    for item in tmp1:
        keypoints2.append(list(map(int, item.split(' '))))
    file.close()

    # simpleResize(image1File, image2File)
    # image2Resize = cv2.imread('aligned.jpg')

    for key in keypoints2:
        key[0] = key[0] * xScale
        key[1] = key[1] * yScale

    keypoints1NP = np.asarray(keypoints1, dtype=np.float32)
    keypoints2NP = np.asarray(keypoints2, dtype=np.float32)

    

    transform = cv2.getAffineTransform(keypoints1NP, keypoints2NP)

    aligned = cv2.warpAffine(image2, transform, (width, height))

    cv2.imwrite('aligned.jpg', aligned)



def simpleResize(image1File, image2File):

    image1 = cv2.imread(image1File)
    image2 = cv2.imread(image2File)

    height, width, c = image1.shape

    aligned = cv2.resize(image2, (width, height))

    cv2.imwrite('aligned.jpg', aligned)

    return