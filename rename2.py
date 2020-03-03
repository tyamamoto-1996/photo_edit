from PIL import Image
import glob
import re
import os

'''
指定したフォルダ内のすべてのjpgファイルを(フォルダ名).jpg、…と名前を変更し
別フォルダに保存し直すスクリプト
'''
#元画像フォルダ
in_path = 'C://Users//AIH_Guest//Desktop//Eye_position//program//Int_photo//*'
#保存先フォルダ
out_path = 'C://Users//AIH_Guest//Desktop//Eye_position//program//Int_photo_rename'


def main():
    path = glob.glob(in_path + '//*.jpg')

    k = 0
    x = 0
    for i in range(len(path)):
        dir = os.path.dirname(path[x])
        dirname = dir.lstrip('C://Users//AIH_Guest//Desktop//Eye_position//program//Int_photo')
        x += 1
        im = Image.open(path[k])
        im.save(out_path + '//i' + dirname[1:] + '.jpg')
        print(os.path.basename(path[k]) + ' Done')
        k += 1

main()