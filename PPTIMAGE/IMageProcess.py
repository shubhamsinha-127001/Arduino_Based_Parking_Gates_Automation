import os
import sys
import time

import cv2
import matplotlib.pyplot as plt
import psycopg2
import psycopg2.extras
import pytesseract


def plot_images(img1, img2, title1="", title2=""):
    fig = plt.figure(figsize=[15, 15])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img1, cmap="gray")
    ax1.set(xticks=[], yticks=[], title=title1)

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2, cmap="gray")
    ax2.set(xticks=[], yticks=[], title=title2)


def ImageExtraction():
    isexist = os.path.exists("E:\Projects\MIC\FlaskAndReact\ImageProcessing\Images\Ger7.jpg")

    if isexist:
        testimage = "E:\Projects\MIC\FlaskAndReact\ImageProcessing\Images\z.jpg"
        print(testimage)
        image = cv2.imread(testimage)

        image = cv2.resize(image, None, fx=0.5, fy=0.5)
        imageres = cv2.resize(image, None, fx=0.5, fy=0.5)

        plot_images(image, imageres)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blur = cv2.bilateralFilter(gray, 11, 90, 90)

        edges = cv2.Canny(blur, 30, 200)

        cnts, new = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        image_copy = image.copy()

        _ = cv2.drawContours(image_copy, cnts, -1, (255, 0, 255), 2)

        #report = cv2.drawContours(edges, cnts, -1, (255, 0, 255), 2)
        plot_images(edges, _)

        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

        image_copy = image.copy()
        _ = cv2.drawContours(image_copy, cnts, -1, (255, 0, 255), 2)
        plot_images(image, _)
        plate = None
        for c in cnts:
            perimeter = cv2.arcLength(c, True)
            edges_count = cv2.approxPolyDP(c, 0.02 * perimeter, True)
            # print(len(edges_count))
            if len(edges_count) == 4:
                x, y, w, h = cv2.boundingRect(c)
                plate = image[y:y + h, x:x + w]
                break

        cv2.imwrite("platea.png", plate)
        plot_images(plate, plate)

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tes' \
                                                r'seract-OCR\tesseract.exe'
        RetrivedLisNummer = pytesseract.image_to_string(plate,
                                                        config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
        # text = pytesseract.image_to_string(plate, config='--psm 7')
        print(RetrivedLisNummer)
        print("after stripping::::::")
        print(RetrivedLisNummer.strip())
        if RetrivedLisNummer == '' or len(RetrivedLisNummer) < 5:

            print("Image is not clear, pleae take another image")
            return "Image is not clear, pleae take another image"
        else:
            return RetrivedLisNummer

    else:

        print("SORRY CANT PROCEED FURTHER, IMAGE WAS NOT FOUND FOR PROCESSING")
        return "SORRY CANT PROCEED FURTHER, IMAGE WAS NOT FOUND FOR PROCESSING"

ImageExtraction()