import numpy as np
import cv2


def rotateimg(img, deg):
    rows = img.shape[0]
    cols = img.shape[1]

    M = cv2.getRotationMatrix2D((cols/2,rows/2),deg,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst


def zoomimg(img):
    rows = img.shape[0]
    cols = img.shape[1]
    pts1 = np.float32([[0,0],[720,0],[1280,0],[720,720]])
    #pts1 = np.float32([[0,0],[0,720],[0,1280],[1280,720]])
    pts2 = np.float32([[0,0],[960,0],[1280,0],[960,960]])
    #pts2 = np.float32([[0,0],[0,960],[0,1280],[1280,860]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(960,960))

    return dst

def zoom2 (image,x):
    r = x / image.shape[1]
    dim = (int(x), int(image.shape[0] * r))

    # perform the actual resizing of the image and show it
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized


# Load an color image in grayscale
img = cv2.imread('1.jpg')
#1280 960
img2 = cv2.imread('2.jpg')
#1280 720

img1 = rotateimg(img,7)

img2 = zoom2(img2, 500)
img1 = zoom2(img1, 500)
img11 = img1[:,50:500]
img21 = img2[50:716,25:475]

vis = np.concatenate((img11, img21), axis=1)

fin_img = img11
index = [10,22,9,14,11,15,30,20,10,29,15,9,33,23]
i = 0
k = 0
for j in index:
    if k == 0 :
        fin_img[:,250+i:250+i+j-1] = img21[:,250+i:250+i+j-1]
        fin_img[:,250-i-j+1:250-i] = img21[:,250-i-j+1:250-i]
        k = 1
    else:
        k = 0
    i = i + j

cv2.imwrite('img.jpg', vis)
cv2.imwrite('fin.jpg', fin_img)
