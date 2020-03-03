import cv2
from PIL import Image
import glob
import re
import os

eye_cascade_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//haarcascades//haarcascade_eye.xml'
face_cascade_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//haarcascades//haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

#元画像フォルダ
in_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//Int_photo_rename'
#保存先フォルダ
out_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//Int_photo_eyes2'

def eyes_cutout():
    path = glob.glob(in_path + '//*.jpg')
    margin = 100
    k = 0
    for i in range(len(path)):
        src = cv2.imread(path[k])
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(src_gray)
        imcv2 = cv2.imread(path[k])
        height, width, channel = imcv2.shape

        left = 10000
        right = 0
        upper = 10000
        lower = 0
        num_of_eyes = 0

        for (ex, ey, ew, eh) in eyes:
            if ew < 150 or eh < 150:    #幅150px以下、高さ150px以下のものは眼としない
                continue
            else:
                cv2.rectangle(src, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                if ex < left:
                    if ex > margin:
                        left = ex - margin
                    else:
                        left = 0
                if ey < upper:
                    if ey > margin:
                        upper = ey - margin
                    else:
                        upper = 0
                if ex + ew > right:
                    if ex + ew + margin < width:
                        right = ex + ew + margin
                    else:
                        right = width
                if ey + eh > lower:
                    if ey + eh + margin < height:
                        lower = ey + eh + margin
                    else:
                        lower = height
                num_of_eyes += 1

        if left == 10000 or upper == 10000:
            print(os.path.basename(path[k]) + ' is skipped because it has 0 eyes')
        if num_of_eyes != 2:
            print(os.path.basename(path[k]) + ' is skipped because it hes ' + str(num_of_eyes) + ' eyes')
        else:
            im = Image.open(path[k])
            im_crop = im.crop((left, upper, right, lower))
            im_crop.save(out_path + '//'+ os.path.basename(path[k]))
            print(os.path.basename(path[k]) + ' Done')

        k += 1

if __name__ == '__main__':
    eyes_cutout()