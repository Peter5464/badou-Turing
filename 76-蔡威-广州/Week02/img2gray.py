# *__* coding:UTF-8 *__*
# 开发团队：时光少年
# 开发人员：Peter Bell
# 开发时间：2021/7/8 2:00
# 文件名称： img2gray.py
# 开发工具： PyCharm


import numpy as np
import cv2


def img_gray(img):
    height, width = img.shape[:2]
    dst_img = np.zeros((height, width), img.dtype)
    for i in range(height):
        for j in range(width):
            src_img = img[i, j]
            dst_img[i, j] = int(0.11*src_img[0] + 0.59*src_img[1] + 0.3*src_img[2])  # RGB -> GBR 的灰度转换
    return dst_img


if __name__ == '__main__':
    img0 = cv2.imread("lenna.png")
    dst_img0 = img_gray(img0)
    test_img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    print(dst_img0)
    print(test_img0)
    cv2.imshow("cv2_pic", img0)
    cv2.imshow("b2g_pic", dst_img0)
    cv2.imshow("cv2_b2g_pic", test_img0)
    cv2.waitKey(0)
