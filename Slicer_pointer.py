# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:36:34 2024

@author: te19p781
"""

# -*- coding: utf-8 -*-

import os, glob, shutil
from PIL import Image
import cv2 as cv

def all_in():
    loc = r"C:\Users\te19p781\Desktop\ggg\Cube_2x2"
    loc_1 = os.path.join(loc,"*")
    loc_mother_file = glob.glob(loc_1)
    for i in loc_mother_file:
        print(i)
        localisator(i)

def localisator(files):
    list_of_file = files

    all_path = os.path.join(list_of_file, "*.tif")
    all_image = glob.glob(all_path)
    new_path = os.path.join(list_of_file,"Slice")
    n = 0
    len_doc = len(all_image)
    for i in all_image:
        slice_renamer(i)
    all_path = os.path.join(list_of_file, "*.tif")
    all_image = glob.glob(all_path)
    
    while n< len_doc:
            
        transfere = all_image[n].replace(list_of_file, new_path)
            
        os.makedirs(os.path.dirname(transfere), exist_ok=True)
        shutil.copy2(all_image[n], transfere) 
        n = n +14
        pointer(transfere)
   
def slice_renamer(img): #rename the file in the correct format
    place = img.rfind("_") + 1 
    lenght = len(img[place:])
    if lenght == 5:
        
        a = list(img)
        a.insert(place,"00")
        img2 =  "".join(a)
        shutil.copy2(img, img2)
        os.remove(img)
    elif lenght == 6:
        a = list(img)
        a.insert(place,"0")
        img2 =  "".join(a)
        shutil.copy2(img, img2)        
        os.remove(img)
def pointer(img): #do the drawing of the image
    imag = Image.open(img)
    jpeg_image = imag.convert("RGB")
    save_path = img.replace(".tif",".jpg")
    jpeg_image.save(save_path)
    imag_2 = cv.imread(save_path)
    larg, leng = imag.size
    
    
    size_of_jump = int( leng / 9) # define the number of point
    size_of_jump_x = int(larg / 12) # define the number of poin
    st_point = int(size_of_jump/2)
    st_point_x = int(size_of_jump_x/2)
    n = 1
    while n < 13:
        l = 1
        while l<10:
            
            if n == 1 and l ==1:
                
                imag_2[st_point:(st_point+2),st_point_x:(st_point_x+2)] = [0,255,0]
            elif n == 1 and l != 1:
                point_y = size_of_jump*(l-1) + st_point
                imag_2[point_y:(point_y+2),st_point_x:(st_point_x+2)] = [0,255,0]
            elif n != 1 and l ==1:
                point_x = size_of_jump_x*(n-1) + st_point_x
                imag_2[st_point:(st_point+2),point_x:(point_x+2)]= [0,255,0]
            else:
                point_x = size_of_jump_x*(n-1)+ st_point_x
                point_y = size_of_jump*(l-1) + st_point
                imag_2[point_y:(point_y+2),point_x:(point_x+2)] = [0,255,0]
            l = l+1
        n = n+1
    cv.imwrite(save_path, imag_2)
all_in()
