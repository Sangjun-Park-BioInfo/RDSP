#
#
#  Student ID: 2018101831
#  Name: 박상준
#
#


from pickletools import uint1
import pickletools
import numpy as np
import cv2 as cv

class homework:

    def bright_contrast(self, img, a, b):
        
        img_result = np.zeros(img.shape, dtype=np.ubyte)

        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                img_result[y, x] = np.clip((img[y, x]/255.0) ** b * 255 + a, 0, 255)
               
        
        return img_result

    def dege_detection(self, img):
        img_result = cv.Canny(img, 100, 200)
        return img_result

    def zoom(self, img, z):
        #Determine zoomed space
        space = [int(img.shape[i] * z) for i in range(2)]

        #Make zoomed image
        img_zoom = np.zeros([space[0], space[1], 3], dtype = np.ubyte)
        for y in range(img_zoom.shape[0]):
            for x in range(img_zoom.shape[1]):
                img_zoom[y, x] = np.clip(img[int(y / z), int(x / z)], 0, 255)

        
        
        #Paste zoom image to orignal size
        if z >= 1:
            cen = [round(img_zoom.shape[0] / 2), round(img_zoom.shape[1] / 2)]
            img_result = img_zoom[cen[0] - 240 : cen[0] + 240,
            cen[1] - 320 : cen[1] + 320 ]

        elif z < 1:
            img_result = np.zeros(img.shape, img.dtype)
            cen = [round(img_result.shape[0] / 2), round(img_result.shape[1] / 2)]

            img_result[cen[0] - round(img_zoom.shape[0]/2) :
                cen[0] + round(img_zoom.shape[0]/2),
                    cen[1] - round(img_zoom.shape[1]/2) :
                        cen[1] + round(img_zoom.shape[1]/2)] = img_zoom



        return img_result


    def rotation(self, img, r):

        img_result = np.zeros(img.shape, img.dtype)
        
        r = np.pi / 180 * r 
        hh = np.int(img.shape[0]/2)
        ww = np.int(img.shape[1]/2) 
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                img_x = np.int(np.cos(r) * (x-ww) - np.sin(r) * (y-hh))+ww
                img_y = np.int(np.sin(r) * (x-ww) + np.cos(r) * (y-hh))+hh
                if img_x < 0 or img_x >= img.shape[1] or img_y < 0 or img_y >= img.shape[0]:
                    continue
                img_result[y, x] = img[img_y, img_x]
        
        return img_result

    def denoising(self, img):
        
        img_result = cv.GaussianBlur(img, (3,3), 0)
        return img_result

