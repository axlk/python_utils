#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import re
import sys
import time
import os
from org_ax_htmlutil import *
import urllib.parse


#huizong_url = sys.argv[1]
#domain_name = sys.argv[2]


#所有参数, 可改成外部
#huizong_url = "http://f.uliba.net/category/flhz"

#开始页面以及url
huizong_start_idx = 1
huizong_end_idx = 10000
huizong_url = " http://f.uliba.net/category/flhz/page/"

#内容表达式
find_article_re = "<article.*</article>"
domain_name="f.uliba.net"

#是否保存图片
save_image_flag=1

#寻找image pattern
find_fuli_image_re_pattern = R"(<img src=.*?)(\.jpg|\.gif|\.png)(.*?/>)"

#图片保存路径
save_path="./save_path/"
if not os.path.exists(save_path):
    os.mkdir(save_path)

"""
==================================================================
#print("huizong url:"+huizong_url+", domain_name:"+domain_name)
"""

#获取福利汇总单页url
def search_fulihuizong_urls( huizong_url, domain_name ):

    response = urllib.request.urlopen(huizong_url)
    page_content = str(response.read(),"utf-8")

    findpattern = R"<a href=\"http:\/\/"+domain_name+"\/.*\.html";
    all_pattern_src = re.findall(findpattern, page_content,flags=re.MULTILINE)

    #print("pattern len ->"+str(len(all_pattern_src)))

    all_href=[]

    tmp_cnt = 0
    for href in all_pattern_src:
        all_href.append( href[9:len(href)])
        #print(all_href[tmp_cnt])
        tmp_cnt = tmp_cnt + 1

    return all_href

#保存福利图片
def save_fuli_images(all_href, find_article_re):
    tmp_cnt = 0
    for huizong_url in all_href:
        #if tmp_cnt == 1:
        #    break

        print("AX --> open url :"+str(huizong_url))
        response = urllib.request.urlopen(huizong_url)
        page_content = str(response.read(),"UTF-8")


        #find_article_re = "<article.*</article>"
        
        article_content = re.findall(find_article_re, page_content, flags=re.MULTILINE+re.DOTALL)[0]
        #print(article_content)

        all_image_url = get_image_url(find_fuli_image_re_pattern,  article_content)

        #汇总名,
        huizong_name=huizong_url.split("/")[-1].split(".")[0];
        #将中文编码换回中文
        huizong_name=urllib.parse.unquote(huizong_name)
        huizong_path=save_path+"/"+huizong_name

        print("huizong path :"+huizong_name)
        if not os.path.exists(huizong_path):
            os.mkdir(huizong_path)

        for image in all_image_url:

            base_name = os.path.basename(image) #图片文件名

            write_image=huizong_path+"/"+base_name

            print("download image ---> :"+str(write_image))
            if bool(save_image_flag):
                #图片名重名处理
                if os.path.exists(write_image):
                    base_name_split = base_name.split(".")
                    base_name = base_name_split[0]+"_new"+"."+base_name_split[1]
                    write_image=huizong_path+"/"+base_name

                urllib.request.urlretrieve(image, write_image)
                time.sleep(0.1)

        tmp_cnt += 1 
        print("-------------------------\n\n")
        time.sleep(1)

#搜索所有页面
tmp_cnt = 0
for i in range(huizong_start_idx, huizong_end_idx):
    #if tmp_cnt == 1:
    #    break
    try:
       search_url = huizong_url+str(i)
       #print(search_url)
       #汇总URL,单页
       print("process url :"+search_url)
       all_href = search_fulihuizong_urls(search_url, domain_name)
       save_fuli_images(all_href, find_article_re)
       time.sleep(2)
    except Exception as errstr:
        print("over at "+str(i)+"page!")
        print("err msg:"+errstr)
        break

    tmp_cnt += 1
