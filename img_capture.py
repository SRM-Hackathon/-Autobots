from __future__ import print_function
import sys
import cv2


def main(argv):
    #capture from camera at location 0
    cap = cv2.VideoCapture(0)
    test = cap.get(cv2.cv.CV_CAP_PROP_POS_MSEC)
    ratio = cap.get(cv2.cv.CV_CAP_PROP_POS_AVI_RATIO)
    frame_rate = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    width = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    brightness = cap.get(cv2.cv.CV_CAP_PROP_BRIGHTNESS)
    contrast = cap.get(cv2.cv.CV_CAP_PROP_CONTRAST)
    saturation = cap.get(cv2.cv.CV_CAP_PROP_SATURATION)
    hue = cap.get(cv2.cv.CV_CAP_PROP_HUE)
    gain = cap.get(cv2.cv.CV_CAP_PROP_GAIN)
    exposure = cap.get(cv2.cv.CV_CAP_PROP_EXPOSURE)
    print("Test: ", test)
    print("Ratio: ", ratio)
    print("Frame Rate: ", frame_rate)
    print("Height: ", height)
    print("Width: ", width)
    print("Brightness: ", brightness)
    print("Contrast: ", contrast)
    print("Saturation: ", saturation)
    print("Hue: ", hue)
    print("Gain: ", gain)
    print("Exposure: ", exposure)
    while True:
        ret, img = cap.read()
        cv2.imshow("input", img)

        key = cv2.waitKey(10)
        if key == 27:
            break

    cv2.destroyAllWindows()
    cv2.VideoCapture(0).release()

if __name__ == '__main__':
    main(sys.argv)