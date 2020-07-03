import json
import cv2
import numpy as np
import os
 
def cvt_one(json_path,img_path,save_path):
    # load img and json
    data = json.load(open(json_path))
    img = cv2.imread(img_path)
 
    # show keys
    #for key in data:
        #print(key)
 
    # get background data
    img_h = data['imageHeight']
    img_w = data['imageWidth']
    color_bg = (0, 0, 0)
    points_bg = [(0, 0), (0, img_h), (img_w, img_h), (img_w, 0)]
    img = cv2.fillPoly(img, [np.array(points_bg)], color_bg)
 
    # get raw roi data
    color_cmyk = []
    points = []
    for content in data['shapes']:
        color_cmyk.append(content['fill_color'])
        points.append(content['points'])
 
    # cmyk 2 rgb
    color_rgb = []
    for color in color_cmyk:
        c = color[0]
        m = color[1]
        y = color[2]
        k = color[3]
        r = 255 * (100 - c) * (100 - k) / 10000
        g = 255 * (100 - m) * (100 - k) / 10000
        b = 255 * (100 - y) * (100 - k) / 10000
        color_rgb.append([r, g, b])
 
    #print(color_rgb)
 
    # draw ROI
    num = len(color_rgb)
    index = 0
    while index < num:
        img = cv2.fillPoly(img, [np.array(points[index])], color_rgb[index])
        index = index + 1
 
    cv2.imwrite('%s'%save_path, img)
 
 
if __name__ == '__main__':
 
    # load imgs and jsons dir
    file_dir = './JPEGImages'
    save_dir = './labels'
    file_path = os.listdir(file_dir)
    total_num = len(file_path)/2
    flag = 0
    while flag < total_num:
        json_path = file_dir+'/'+file_path[flag*2+1]
        img_path = file_dir+'/'+file_path[flag*2]
        save_path = save_dir+'/'+file_path[flag*2]
        cvt_one(json_path, img_path, save_path)
        flag = flag + 1