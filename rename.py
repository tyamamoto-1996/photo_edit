from PIL import Image
import glob
import re
import os

'''
指定したフォルダ内のすべてのjpgファイルを0.jpg、1.jpg、…と名前を変更し
別フォルダに保存し直すスクリプト
'''
#元画像フォルダ
in_path = 'C://Users//AIH_Guest//Desktop//Eye_position//program//Int_photo//*'
#保存先フォルダ
out_path = 'C://Users//AIH_Guest//Desktop//Eye_position//program//Int_photo_rename'

def main():
    path = glob.glob(in_path + '//*.jpg')

    k=0
    for i in range(len(path)):
        im = Image.open(path[k])
        im.save(out_path + '//i' + str(k) + '.jpg')
        print(os.path.basename(path[k]) + ' Done')
        k+=1

main()