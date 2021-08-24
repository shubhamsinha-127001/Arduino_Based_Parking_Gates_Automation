import os
import sys
import time

import cv2
import matplotlib.pyplot as plt
import psycopg2
import psycopg2.extras
import pytesseract


# from serial import Serial
import serial as serial


def plot_images(img1, img2, title1="", title2=""):
    fig = plt.figure(figsize=[15, 15])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img1, cmap="gray")
    ax1.set(xticks=[], yticks=[], title=title1)

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2, cmap="gray")
    ax2.set(xticks=[], yticks=[], title=title2)


def ImageExtraction():
    isexist = os.path.exists('Images/Image.jpg')

    if isexist:
        testimage = "./Images/Ger6.jpg"
        print(testimage)
        image = testimage
        (testimage)

        image = cv2.resize(image, None, fx=0.5, fy=0.5)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blur = cv2.bilateralFilter(gray, 11, 90, 90)

        edges = cv2.Canny(blur, 30, 200)

        cnts, new = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        image_copy = image.copy()

        _ = cv2.drawContours(image_copy, cnts, -1, (255, 0, 255), 2)

        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

        image_copy = image.copy()
        _ = cv2.drawContours(image_copy, cnts, -1, (255, 0, 255), 2)

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


def CheckAllLisenceNumberExistance(LisenceNumber):
    print("INSIDE FETCHING NUMBER::::")
    global DB_HOST, DB_NAME, DB_USER, DB_PASS
    DB_HOST = "localhost"
    DB_NAME = "MIC_PROJECT_PARKING"
    DB_USER = "postgres"
    DB_PASS = "admin"
    conn = None

    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    except:
        print('UNKNOW ERROR while creating database connection::::', sys.exc_info()[0])

    if conn is not None:
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute('select emp_vech_number from emp_vec_details')
                tup = (cur.fetchall())
                print(tup)
                for sublist in tup:
                    if sublist[0] == LisenceNumber:
                        print('njbhgvcfdxfcgvbh')
                        return True
                        break
                return false;
        conn.close()
    else:
        print('Cant insert values, DB connection not created!')


LisenceNumberString = ImageExtraction()
print("asd:::", LisenceNumberString.strip())

vaccantSpace = database.checkVacantSpace()

NumberExist = CheckAllLisenceNumberExistance(LisenceNumberString.strip())
print("ISESIST::::", NumberExist)

import serial as serial



if NumberExist is True:
    data = "on"

elif NumberExist is False:
    data = "off"

elif vaccantSpace <= 0:
    data = "full"

print(data)

serialcomm = serial.Serial('COM3', 9600)
serialcomm.timeout = 1
while True:
    # i = input("Enter Input: ").strip()
    # if i == "Done":
    # print('finished')
    # break
    serialcomm.write(data.encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))
serialcomm.close()
