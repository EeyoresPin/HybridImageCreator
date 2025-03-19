from alignment import simpleResize, affineTransform
from spatial_fusion import buildSpatialImage
from frequency_fusion import buildFrequencyImage
import sys




def IfEmpty(filename):

    tmp1= []
    file = open(filename, "r")
    for line in file:
        cleanLine = line.replace('\n','')
        tmp1.append(cleanLine)

    file.close()

    if len(tmp1) > 0:
        return False
    else:
        return True



def main():

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    keyFile1 = sys.argv[3]
    keyFile2 = sys.argv[4]

    #simpleResize(filename1, filename2)
    if IfEmpty(keyFile1) or IfEmpty(keyFile2):
        #print("SIMPLE RESIZE")
        simpleResize(filename1, filename2)
    else:
        #print("AFFINE TRANSFORM")
        affineTransform(filename1, filename2, keyFile1, keyFile2)

    buildSpatialImage(filename1)
    buildFrequencyImage(filename1)
    


if __name__ == '__main__':
    main()




    