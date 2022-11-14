import random
import math
from statistics import mean

def shrink_gap(old_img, new_img, x1, x2, border1):
    width, height = old_img.size
    direction = "left"
    if x1 > x2:
        direction = "right"
    
    pixels_to_shrink = abs(x2 - x1)
    dist_range = random.randrange(pixels_to_shrink*pixels_to_shrink)

    xrange = range(x1, x2)
    if direction == "left":
        xrange = range(x1,x2,-1)

    print(x1, x2)

    for i in range(x1, x2):
        for j in range(height):
            avg_x = 0
            avg_y = 0
            point1RGB = 0
            point2RGB = 0
            if random_shrink_x+1 < width:
                point1RGB = old_img.getpixel((random_shrink_x, j))
                point2RGB = old_img.getpixel((random_shrink_x+1, j))
            else:
                point1RGB = old_img.getpixel((random_shrink_x, j))
                point2RGB = old_img.getpixel((random_shrink_x-1, j))
            newPointRGB = (mean([point1RGB[0], point2RGB[0]]), mean([point1RGB[1], point2RGB[1]]), mean([point1RGB[2], point2RGB[2]]))
    return new_img
    