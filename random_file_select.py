from PIL import Image
import glob
import os
import random

#Cont元画像フォルダ
cont_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//Control_photo_square'
#Exte元画像フォルダ
exte_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//Ext_photo_square'
#Inte元画像フォルダ
inte_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//Int_photo_square'
#保存先フォルダ
out_path = 'C://Users//yuikeru2//Desktop//Eye_position//program//data//hymenoptera_data'

def cont_select():
    path = glob.glob(cont_path + '//*.jpg')

    ratio = 0.7 #trainの割合
    num_of_photo = len(path)
    num_of_train = round(num_of_photo * ratio)
    num_of_val = num_of_photo - num_of_train
    tra_count = 0
    val_count = 0
    k = 0

    for i in range(len(path)):
        im = Image.open(path[k])
        if tra_count >= num_of_train:   #train枚数が上限に到達
            im.save(out_path + '//val//Cont//' + os.path.basename(path[k]))
            val_count += 1
        elif val_count >= num_of_val:   #val枚数が上限に到達
            im.save(out_path + '//train//Cont//' + os.path.basename(path[k]))
            tra_count += 1
        else:
            r = random.random()
            if r < ratio:
                im.save(out_path + '//train//Cont//' + os.path.basename(path[k]))
                tra_count += 1
            else:
                im.save(out_path + '//val//Cont//' + os.path.basename(path[k]))
                val_count += 1
        k += 1

def exte_select():
    path = glob.glob(exte_path + '//*.jpg')

    ratio = 0.7 #trainの割合
    num_of_photo = len(path)
    num_of_train = round(num_of_photo * ratio)
    num_of_val = num_of_photo - num_of_train
    tra_count = 0
    val_count = 0
    k = 0

    for i in range(len(path)):
        im = Image.open(path[k])
        if tra_count == num_of_train:   #train枚数が上限に到達
            im.save(out_path + '//val//Exte//' + os.path.basename(path[k]))
            val_count += 1
        elif val_count == num_of_val:   #val枚数が上限に到達
            im.save(out_path + '//train//Exte//' + os.path.basename(path[k]))
            tra_count += 1
        else:
            r = random.random()
            if r < ratio:
                im.save(out_path + '//train//Exte//' + os.path.basename(path[k]))
                tra_count += 1
            else:
                im.save(out_path + '//val//Exte//' + os.path.basename(path[k]))
                val_count += 1
        k += 1

def inte_select():
    path = glob.glob(inte_path + '//*.jpg')

    ratio = 0.7 #trainの割合
    num_of_photo = len(path)
    num_of_train = round(num_of_photo * ratio)
    num_of_val = num_of_photo - num_of_train
    tra_count = 0
    val_count = 0
    k = 0

    for i in range(len(path)):
        im = Image.open(path[k])
        if tra_count == num_of_train:   #train枚数が上限に到達
            im.save(out_path + '//val//Inte//' + os.path.basename(path[k]))
            val_count += 1
        elif val_count == num_of_val:   #val枚数が上限に到達
            im.save(out_path + '//train//Inte//' + os.path.basename(path[k]))
            tra_count += 1
        else:
            r = random.random()
            if r < ratio:
                im.save(out_path + '//train//Inte//' + os.path.basename(path[k]))
                tra_count += 1
            else:
                im.save(out_path + '//val//Inte//' + os.path.basename(path[k]))
                val_count += 1
        k += 1

cont_select()
exte_select()
inte_select()



