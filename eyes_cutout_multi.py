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
in_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//Control_photo'
#保存先フォルダ
out_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//Control_photo_eyes'

def eyes_cutout():
    path = glob.glob(in_path + '//*.jpg')
    im_black = Image.open('C://Users//yuikeru2//Desktop//Eye_position//program//black.jpg')
    k = 0
    x = 0
    for i in range(len(path)):
        src = cv2.imread(path[k])
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(src_gray)


        left = 10000
        right = 0
        upper = 10000
        lower = 0
        num_of_eyes = 0

        for (ex, ey, ew, eh) in eyes:
            if ew < 250 or eh < 250:    #幅250px以下、高さ250px以下のものは眼としない
                continue
            else:
                cv2.rectangle(src, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                if ex < left:
                    left = ex
                if ey < upper:
                    upper = ey
                if ex + ew > right:
                    right = ex + ew
                if ey + eh > lower:
                    lower = ey + eh
                num_of_eyes += 1

        if left == 10000 or upper == 10000:
            im_black.save(out_path + '//'+ os.path.basename(path[k]))
            print(os.path.basename(path[k]) + ' is skipped because it has 0 eyes')
        elif num_of_eyes != 2:
            im_black.save(out_path + '//' + os.path.basename(path[k]))
            print(os.path.basename(path[k]) + ' is skipped because it hes ' + str(num_of_eyes) + ' eyes')
        else:
            im = Image.open(path[k])
            im_crop = im.crop((left, upper, right, lower))
            im_crop.save(out_path + '//'+ os.path.basename(path[k]))
            print(os.path.basename(path[k]) + ' Done')
            x += 1

        k += 1

    print(str(x) + ' pictures are done')

if __name__ == '__main__':
    eyes_cutout()