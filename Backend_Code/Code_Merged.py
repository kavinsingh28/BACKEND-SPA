import cv2
import numpy as np
import pytesseract


def main():
    frameWidth = 640  # Frame Width
    franeHeight = 480   # Frame Height
    plateCascade = cv2.CascadeClassifier(
        "C:\\Users\\kavin\\OneDrive\\Desktop\\Systematic Parking Accomplisher\\codes\\REsources\\haarcascade_russian_plate_number.xml")
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    minArea = 500

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, frameWidth)
    cap.set(4, franeHeight)
    cap.set(10, 150)
    cap_Img(cap, plateCascade, minArea)


def cap_Img(cap, plateCascade, minArea):
    while True:
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
        for (x, y, w, h) in numberPlates:
            area = w*h
            if area > minArea:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, "NumberPlate", (x, y-5),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                imgRoi = img[y:y+h, x:x+w]
                cv2.imshow("ROI", imgRoi)

        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(
                "C:/Users/kavin/OneDrive/Desktop/Systematic Parking Accomplisher/codes/Saved_Images/New.jpg", imgRoi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Scan Saved", (15, 265),
                        cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
            cv2.imshow("Result", img)
            cv2.waitKey(100)
            break


def read_Img():
    img = cv2.imread(
        "C:/Users/kavin/OneDrive/Desktop/Systematic Parking Accomplisher/codes/Saved_Images/Final.jpg")
    text = pytesseract.image_to_string(img)  # extract text
    print(''.join(text.split()), '\n', text)


if __name__ == "__main__":
    main()
    read_Img()
