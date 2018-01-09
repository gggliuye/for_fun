import cv2
import numpy as np


def insert(imgo,img,pos):
  height = img.shape[0]
  width = img.shape[1]
  by = pos[0]
  bx = pos[1]
  ox = 0
  oy = 0
  for c in range(0,3):
    alpha = 1.0 - img[oy:oy+height, ox:ox+width, c] / 255.0
    alpha = alpha.astype(int)
    color = img[oy:oy+height, ox:ox+width, c] * (1.0-alpha)
    beta  = imgo[by:by+height, bx:bx+width, c] * (alpha)
    imgo[by:by+height, bx:bx+width, c] = color + beta

img = cv2.imread('black_mirror.jpg')
im_src = cv2.imread('2.jpg')
#960 * 1280
imt = cv2.imread('timessquare.jpg')
#1000 * 1500

pts_src = np.array([[0,0],[0,960],[1280,960],[1280,0]])
pts_dst = np.array([[450,700],[445,800],[600,810],[605,690]])
#pts_dst = np.array([[700,440],[870,450],[80,607],[690,650]])

h, status = cv2.findHomography(pts_src, pts_dst)
size = (1000,1000)
im_dst = cv2.warpPerspective(im_src, h, size)


insert(imt,im_dst,[0,0])

cv2.imwrite('img.jpg',imt)
cv2.imwrite('img1.jpg',im_dst)



