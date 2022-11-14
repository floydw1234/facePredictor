import face_recognition
from PIL import Image
from shrink import shrink_gap

def pad_lines(x, y, img, padding):
    for i in range(-padding, padding):
        for j in range(-padding, padding):
            img.putpixel((x + i,y + j), (255,0,0, 255))

def strech_cheeks(old_img, new_img, ratio):
    new_img = shrink_gap(old_img,new_img, 200, 400,500)
    new_img.show()
    return new_img
    print("TBI: old_img, new_img")

def stretch(old_img, new_img, x1, y1, x2, y2):
    print("TBI: old_img, new_img")\

def move_cluster(old_img, new_img, x1,y1,x2, y2):
    print("TBI: old, new")

def find_center_line(img):
    print("TBI: mx+b, y-b/m")

