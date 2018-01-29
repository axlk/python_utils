#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re

#file = open("./fulihuizong.html")
#page_content=file.read()

#print("content:"+page_content)

#re_pattern="(<img src=\".*)(\.jpg\|\.png)\">"
#re_pattern="(<p>.*<img .*)(\.jpg|\.png|\.gif)"

#all_image_pattern_src = re.findall(re_pattern, page_content)

#print("catch image len:"+str(len(all_image_pattern_src)))
#print(all_image_pattern_src)

"""
all_image_url = {}
tmp_cnt = 0
for image in all_image_pattern_src:
    start_index = image[0].find("http")
    #all_image_url[tmp_cnt] = image[0][start_index:len(image[0])]+image[1]
    all_image_url[tmp_cnt] = image[0][start_index:len(image[0])]+image[1]
    print(all_image_url[tmp_cnt])
    tmp_cnt = tmp_cnt + 1
"""

def get_image_url( re_pattern, page_content ):
    all_image_pattern_src = re.findall(re_pattern, page_content)
    
    all_image_url = []
    tmp_cnt = 0
    for image in all_image_pattern_src:
        start_index = image[0].find("http")
        #all_image_url[tmp_cnt] = image[0][start_index:len(image[0])]+image[1]
        all_image_url.append( image[0][start_index:len(image[0])]+image[1] )
        #print(all_image_url[tmp_cnt])
    return all_image_url
