from selenium import webdriver
from bs4 import BeautifulSoup

link = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'


def scrapping_data():
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
        print('\n{}\n{}\n{}\nhttps://www.youtube.com{}'.format(title.text, views[i].text, views[i + 1].text,
                                                               video_urls[j].get('href')))
        i += 2
        j += 1


if __name__ == '__main__':
    scrapping_data()