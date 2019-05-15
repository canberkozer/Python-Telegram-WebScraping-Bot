from bs4 import BeautifulSoup
import requests
import time
import telebot

bot_token = "685346294:AAFOQ4u554ouwsNXa2vxGqV11-HTVYdw_T0"
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '(Program başladı. /scrape kullanın)')


@bot.message_handler(commands=['scrape'])
def scrape_page_data(message):
    source_link = "https://www.peopleperhour.com/freelance-jobs?page=1"
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

            bot.reply_to(message, 'Project Name: {}\nPosted Time: {}\nPrice: {} {} {}\nPost Link: {}\n'.format(project_name,posted_time,project_price[0],project_price[1],project_price[2],post_link))  
            break


while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)