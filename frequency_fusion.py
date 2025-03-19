import cv2
import numpy as np

SQUARESIZE = 50

def buildFrequencyImage(filename1):

    image = cv2.imread(filename1)
    aligned = cv2.imread('aligned.jpg')

    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    alignedGray = cv2.cvtColor(aligned, cv2.COLOR_BGR2GRAY)

    high = getHighFrequency(alignedGray)
    low = getLowFrequency(imageGray)

    hybrid = combineFrequencies(low, high)

    cv2.imwrite("frequency_hybrid.jpg", hybrid) 


def getHighFrequency(image):
    fourier = np.fft.fft2(image)
    mask = np.fft.fftshift(fourier)

    rows, cols = image.shape
    crow, ccol = rows//2, cols//2
    mask[crow-SQUARESIZE:crow+SQUARESIZE+1, ccol-SQUARESIZE:ccol+SQUARESIZE+1] = 0
    
    
    return mask

    # fourierInverse = np.fft.ifftshift(mask)
    # imageHigh = np.fft.ifft2(fourierInverse)
    # imageHigh = np.real(imageHigh)
    # imageHigh = cv2.normalize(imageHigh, None, 0, 255, cv2.NORM_MINMAX)
    # imageHigh = np.uint8(imageHigh)
    # cv2.imwrite("testHigh.jpg", imageHigh)

def getLowFrequency(image):
    fourier = np.fft.fft2(image)
    mask = np.fft.fftshift(fourier)

    mask = mask - getHighFrequency(image)
   
       
    return mask

    # fourierInverse = np.fft.ifftshift(mask)
    # imageLow = np.fft.ifft2(fourierInverse)
    # imageLow = np.real(imageLow)
    # imageLow = cv2.normalize(imageLow, None, 0, 255, cv2.NORM_MINMAX)
    # imageLow = np.uint8(imageLow)
    # cv2.imwrite("testLow.jpg", imageLow)

    # return mask

def combineFrequencies(low, high):

    combinedMask = low + high

    fourierInverse = np.fft.ifftshift(combinedMask)

    hybird = np.fft.ifft2(fourierInverse)
    hybird = np.real(hybird)
    hybird = cv2.normalize(hybird, None, 0, 255, cv2.NORM_MINMAX)
    hybird = np.uint8(hybird)

    return hybird