from PIL import Image
import glob
import re
import os

'''
指定したフォルダ内のすべてのjpgファイルを（黒い余白を加えて）正方形にして、
別フォルダに保存し直すスクリプト
'''
#元画像フォルダ
in_path = 'C://Users//AIH_Guest//Desktop//Eye_position//program//Int_photo_rename'
#保存先フォルダ
out_path = 'C://Users//AIH_Guest//Desktop//Eye_position//program//Int_photo_square'


def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width-height)//2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, (0, (height - width) // 2))
        return result


def main():
    path = glob.glob(in_path + '//*.jpg')

    k=0
    for i in range(len(path)):
        im = Image.open(path[k])
        im_new = expand2square(im, (0, 0, 0)).resize((225, 225))
        im_new.save(out_path + '//'+ os.path.basename(path[k]))
        print(os.path.basename(path[k])+ ' Done')
        k+=1

if __name__ == '__main__':
    main()