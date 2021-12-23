from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import json

link = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
json_data = []


def scraping_data():
    driver = webdriver.Chrome()
    driver.get(link)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    titles = soup.findAll('a', id='video-title')
    views = soup.findAll('span', class_='style-scope ytd-video-meta-block')
    video_urls = soup.findAll('a', id='video-title')
    i = 0
    j = 0
    for title in titles:
        # print('\n{}\n{}\n{}\nhttps://www.youtube.com{}'.format(title.text, views[i].text, views[i + 1].text,
        #                                                        video_urls[j].get('href')))

        # save data have beed scraped into json_data variable
        json_data.append({
            'title': title.text.replace("\n",""), # use replace for remove all newline charcode on data
            'views': views[i].text,
            'dates': views[i + 1].text,
            'link': 'https://www.youtube.com' + video_urls[j].get('href')
        })
        i += 2
        j += 1

    extract_data(json_data) # call extract data and pass json_data

    # for title in titles:
    #     json_data.append({
    #         'title' : title,
    #         'title' : title,
    #     })


def extract_data(datas):
    # print(datas)
    # extract data to csv file


    csv_columns = ['title', 'views', 'dates', 'link'] # variable to initial header for column table
    csv_file_name = "youtube_trendings.csv" # filename will be create

    try:
        with open(csv_file_name, 'w',newline='',encoding='utf-8') as csvfile: # command to initial setting to write a file
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns) # command for setup csv file
            writer.writeheader() #command for write header on scv file
            for data in datas:
                writer.writerow(data) # command for write every row to table data
    except IOError:
        print("I/O error")

    # extract data to json file
    try:
        with open("youtube_trendings.json", 'w',newline='',encoding='utf-8') as jsonfile:
            json.dump(datas, jsonfile) # commnad write json data to file
    except IOError:
        print("I/O error")


if __name__ == '__main__':
    scraping_data()
