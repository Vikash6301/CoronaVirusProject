import requests
import bs4

import tkinter as tk
import plyer

import time
import datetime

def get_html_data(url):
    data = requests.get(url)
    return data 


def get_corona_details_of_world():
    url="https://covid19dashboard.mohfw.gov.in/"

    html_data = get_html_data(url)

    bs=bs4.BeautifulSoup(html_data.text,'html.parser')

    info_div= bs.find ("div",class_="col-xs-7 site-stats-count").find("ul").find_all("li")
    #print(info_div)
    for item in info_div[0:2]:
        text = item.find("span",class_="mob-show").get_text()
        count = item.find("strong",class_="mob-hide").get_text()
        print(count)
    
   
get_corona_details_of_world()

