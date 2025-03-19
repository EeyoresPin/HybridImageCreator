# HybridImageCreator
This is a program that takes two images, and creates a hybridised image in both the Spatial Domain, and the Frequency Domain in Object Oriented Python.

To Run:
python3 assignment1.py image1.jpg image2.jpg keypoints1 keypoints2

image1.jpg is the photo you would like to be the low frequency/blurry base to the hybrid image

image2.jpg is the photo you would like to be the high frequency/detailed foreground to the hybrid image

keypoints1 is 3 by 2 file of floating point values repersenting the keypoints you would like to be aligned to for image one

keypoint2 is a 3 by 2 file of floating point values used to adjust image2.jpg to image1.jpg

Output:
This program outputs three files,

aligned1.jpg shows image2.jpg aligned to fit image1.jpg before the hybridisation takes place

frequency_hybrid.jpg shows the hybrid image created, and edited in the frequency domain using a forier transforms.

spatial_hybrid.jpg shows the hybrid image created, and edited in the spatial domain using LaPlacian and Gaussian Pyramids.


