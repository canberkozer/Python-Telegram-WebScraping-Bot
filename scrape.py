from bs4 import BeautifulSoup
import requests
import time

source_link = "https://www.peopleperhour.com/freelance-jobs?page=1"


def scrape_page_data(source_link):
    r = requests.get(source_link)
    soup = BeautifulSoup(r.content, "lxml")

    div_content = soup.find_all(
        'div', attrs={'class': 'clearfix listing-row project-list-item job-list-item '})

    for i in div_content:
        project_name = i.a.text
        posted_time = i.find('time', attrs={'class': 'crop value'}).text.strip()
        project_price = i.find('div', attrs={'class': 'price-tag'}).text.split()
        post_link = i.a['href']

        print("Project Name: ",project_name)
        print("Posted Time: ",posted_time)
        print("Price: {} {} {}".format(project_price[0],project_price[1],project_price[2]))
        print("Post Link: {}\n".format(post_link))

#scrape_page_data(source_link)
#Tek bir sayfadaki verileri çekme.
###########################################################################################################################

def last_24_hours():
    page_number = 1

    while page_number <= 20:
        page_link = 'https://www.peopleperhour.com/freelance-jobs?' + 'page=' + str(page_number)
        source_link = page_link
        
        r = requests.get(source_link)
        soup = BeautifulSoup(r.content, "lxml")

        div_content = soup.find_all(
            'div', attrs={'class': 'clearfix listing-row project-list-item job-list-item '})

        for i in div_content:
            project_name = i.a.text
            posted_time = i.find('time', attrs={'class': 'crop value'}).text.strip()

            if(posted_time == '1 day ago'):
                break

            print("Project Name: ",project_name)
            print("Posted Time: ",posted_time)

            project_price = i.find('div', attrs={'class': 'price-tag'}).text.split()
            print("Price: {} {} {}".format(project_price[0],project_price[1],project_price[2]))

            post_link = i.a['href']
            print("Post Link: {}\n".format(post_link))

        page_number += 1


#last_24_hours() 
#Sadece son 24 saat içerisindeki verileri çeker.
###########################################################################################################################

def last_project(source_links):
    r = requests.get(source_link)
    soup = BeautifulSoup(r.content, "lxml")
    div_contents = soup.find_all('div', attrs={'class': 'clearfix listing-row project-list-item job-list-item '})
    
    for i in div_contents:
        try:
            featured_project = i.find('span', attrs={'class':'etiquette blue'}).text.strip()

        except:
            project_name = i.a.text
            posted_time = i.find('time', attrs={'class': 'crop value'}).text.strip()
            project_price = i.find('div', attrs={'class': 'price-tag'}).text.split()
            post_link = i.a['href']

            print("Project Name: ",project_name)
            print("Posted Time: ",posted_time)               
            print("Price: {} {} {}".format(project_price[0],project_price[1],project_price[2]))                
            print("Post Link: {}\n".format(post_link))

            break

#last_project(source_link)
#öne çıkarılmayan son projeyi verir.
###########################################################################################################################


def endless_scrape():
    while True:
        print(time.strftime('%X\n'))
        last_project(source_link)
        print("************************************************************************************************************************************")
        time.sleep(60)

endless_scrape()

#Yapılacaklar
#Son jobs yazdırılmış ise tekrar yazdırma. 
