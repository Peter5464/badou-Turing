# *__* coding:UTF-8 *__*
# 开发团队：时光少年
# 开发人员：Peter Bell
# 开发时间：2021/7/8 1:09
# 文件名称： nearest_interpolation.py
# 开发工具： PyCharm


import numpy as np
import cv2


def nearest_interpolation(img):
    height, width = img.shape[:2]
    dst_img = np.zeros((880, 880, 3), np.uint8)  # 880*880
    '''图像的比例系数'''
    sh = 880/height
    sw = 880/width
    for i in range(880):
        for j in range(880):
            dst_height = int(i/sh)
            dst_width = int(j/sw)
            dst_img[i, j] = img[dst_height, dst_width]
    return dst_img


if __name__ == '__main__':
    img0 = cv2.imread("lenna.png")
    dst_img0 = nearest_interpolation(img0)
    print(dst_img0.shape)
    print(dst_img0)
    cv2.imshow("cv2_pic", img0)
    cv2.imshow("nearest_inter_pic", dst_img0)
    cv2.waitKey(0)
