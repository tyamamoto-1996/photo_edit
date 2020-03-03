import cv2
from PIL import Image
import os

eye_cascade_path = 'C://Users//AIH_Guest/Desktop//Eye_position//program//haarcascades//haarcascade_eye.xml'
face_cascade_path = 'C://Users//AIH_Guest//Desktop//Eye_position//program//haarcascades//haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

photo = 'C://Users//AIH_Guest//Desktop//Eye_position//program//woman.jpg'
src = cv2.imread(photo)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(src_gray)


left = 10000
right = 0
upper = 10000
lower = 0
num_of_eyes = 0

for (ex, ey, ew, eh) in eyes:
    if ew < 100 or eh < 100:    #幅100px以下、高さ100px以下のものは眼としない
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
    print(os.path.basename(photo) + ' is skipped because it has 0 eyes')
if num_of_eyes != 2:
    print(os.path.basename(photo) + ' is skipped because it has ' + str(num_of_eyes) + ' eyes')
    cv2.imwrite('C://Users//AIH_Guest//Desktop//Eye_position//program//woman_eyes.jpg', src)
else:
    cv2.imwrite('C://Users//AIH_Guest//Desktop//Eye_position//program//woman_eyes.jpg', src)

    im = Image.open(photo)
    im_crop = im.crop((left, upper, right, lower))
    im_crop.save('C://Users//AIH_Guest//Desktop//Eye_position//program//woman_eyes_cut.jpg', quality=95)