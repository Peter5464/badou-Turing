# *__* coding:UTF-8 *__*
# 开发团队：时光少年
# 开发人员：Peter Bell
# 开发时间：2021/7/8 1:37
# 文件名称： bilinear_interpolation.py
# 开发工具： PyCharm


import numpy as np
import math
import cv2


def bilinear_interpolation(img):
    height, width, channels = img.shape
    dst_ht, dst_wh = 880, 880
    dst_img = np.zeros((dst_ht, dst_wh, channels), np.uint8)
    for i in range(dst_ht):
        for j in range(dst_wh):
            x = (i+0.5)/dst_ht*height - 0.5
            y = (j+0.5)/dst_wh*width - 0.5
            '''向下取整'''
            x_int = math.floor(x)
            y_int = math.floor(y)

            '''横纵二维单位偏移量'''
            u = x - x_int
            v = y - y_int

            '''防止溢出'''
            if x_int == height-1 or y_int == width-1:
                x_int = x_int - 1
                y_int = y_int - 1

            '''双线性插值公式'''
            dst_img[i][j] = (1 - u)*(1 - v)*img[x_int][y_int] + (1 - u)*v*img[x_int][y_int + 1]\
                            + u*(1 - v)*img[x_int+1][y_int] + u*v*img[x_int + 1][y_int + 1]
    return dst_img


if __name__ == '__main__':
    img0 = cv2.imread("lenna.png")
    dst_img0 = bilinear_interpolation(img0)
    print(dst_img0.shape)
    print(dst_img0)
    cv2.imshow("cv2_pic", img0)
    cv2.imshow("bilinear_inter_pic", dst_img0)
    cv2.waitKey(0)
