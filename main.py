import datetime
import requests
from bs4 import BeautifulSoup as bs
import json

count = 1

# data = []  
# while count < 338:

#     URL_TEMPLATE = f"https://store.playstation.com/ru-ua/pages/browse/{count}"
#     r = requests.get(URL_TEMPLATE)
#     soup = bs(r.text, "lxml")
#     game_name = soup.find_all('span', class_='psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2')
#     img = soup.find_all('span', class_='psw-media-frame psw-fill-x psw-image psw-media psw-media-interactive psw-aspect-1-1')
#     link = soup.find_all('a', class_='psw-link psw-content-link')

#     for gm, i, li in zip(game_name, img, link):
#         x = i.img['src'].replace('?w=54', '?w=230')
#         x = x.replace('thumb=true', 'thumb=false')

#         data.append({"name: " : gm.text, "img":  x, "link": 'https://store.playstation.com' + li['href']})

#     count+=1
#     print('Статус', r.status_code, 'Страница', count)



with open('test.json') as f:
    templates = json.load(f)

print(templates[0])
# templates[0]['addons'] = [1, 2 ,3 ]


# print(len(templates))
check = True
count = 0
while check != False:
    for i in templates:
        print(i['link'])
        if not i['link']:
            check = False
        URL_TEMPLATE = i['link']
        r = requests.get(URL_TEMPLATE)
        soup = bs(r.text, "lxml")
    # platforms = soup.find_all('dd', class_='psw-p-r-6 psw-p-r-0@tablet-s psw-t-bold psw-l-w-1/2 psw-l-w-1/6@tablet-s psw-l-w-1/6@tablet-l psw-l-w-1/8@laptop psw-l-w-1/6@desktop psw-l-w-1/6@max')
    # platforms = soup.find_all(attrs={'class': 'psw-p-r-6 psw-p-r-0@tablet-s psw-t-bold psw-l-w-1/2 psw-l-w-1/6@tablet-s psw-l-w-1/6@tablet-l psw-l-w-1/8@laptop psw-l-w-1/6@desktop psw-l-w-1/6@max',
    #                                  'data-qa': "gameInfo#releaseInformation#platform-value"})

    # release = soup.find_all(attrs={'class': 'psw-p-r-6 psw-p-r-0@tablet-s psw-t-bold psw-l-w-1/2 psw-l-w-1/6@tablet-s psw-l-w-1/6@tablet-l psw-l-w-1/8@laptop psw-l-w-1/6@desktop psw-l-w-1/6@max',
    #                                  'data-qa': "gameInfo#releaseInformation#releaseDate-value"})


    # genre = soup.find_all(attrs={'class': 'psw-p-r-6 psw-p-r-0@tablet-s psw-t-bold psw-l-w-1/2 psw-l-w-1/6@tablet-s psw-l-w-1/6@tablet-l psw-l-w-1/8@laptop psw-l-w-1/6@desktop psw-l-w-1/6@max',
    #                                  'data-qa': "gameInfo#releaseInformation#genre-value"})

    # publisher = soup.find_all(attrs={'class': 'psw-p-r-6 psw-p-r-0@tablet-s psw-t-bold psw-l-w-1/2 psw-l-w-1/6@tablet-s psw-l-w-1/6@tablet-l psw-l-w-1/8@laptop psw-l-w-1/6@desktop psw-l-w-1/6@max',
    #                                  'data-qa': "gameInfo#releaseInformation#publisher-value"})

    # age_rate = soup.find_all('span', class_='psw-media-frame psw-fill-x psw-image psw-media psw-l-w-icon-4 psw-media-interactive psw-aspect-5-6')

    # title = soup.find_all('h1', class_='psw-m-b-5 psw-t-title-l psw-t-size-8 psw-l-line-break-word')
    # if not title:
    #     title = soup.find_all('h1', class_='psw-m-b-5 psw-t-title-l psw-t-size-7 psw-l-line-break-word')
    #     if not title:
    #         title = soup.find_all('h1', class_='psw-m-b-5 psw-t-title-l psw-t-size-6 psw-l-line-break-word')
    #         if not title:
    #             title = soup.find_all('h1', class_='psw-m-b-5 psw-t-title-l psw-t-size-5 psw-l-line-break-word')

        level = soup.find_all('a', class_='psw-link psw-content-link')

        # print("LEVEL", level)
        addons = []
        for level in level:
            if level.section.span.text == 'Уровень': 
                    addons.append(level['href'])
            if level.section.span.text == 'Дополнение': 
                    addons.append(level['href'])
        # print(addons)
        # print(i)
        templates[count]['addons'] = addons
        with open('test.json', 'w') as f:
            # json.dump(templates, file, ensure_ascii=False)
            json.dump(templates, f, ensure_ascii=False, indent=4)
            # file.write('\n')
        count+=1
    # print(title)
    # s = title[0].text
    # clear_str = s[:s.find(' — ')]
    # clear_str = clear_str.replace('™', '')
    # clear_str = clear_str.replace('®', '')
    # clear_str = clear_str.replace('«', '')
    # clear_str = clear_str.replace('»', '')
    # clear_str = clear_str.replace(':', '')
    # clear_str = clear_str.replace('  ', ' ')
    # clear_str = clear_str.replace('   ', ' ')
    # print (clear_str.replace(' ', '_'))

    # for g in genre:
    #     print(g.text)

    # for x in age_rate:
    #     print(x.img['alt'])

    # for r in release:
    #     date_time_str = r.text
    #     date_time_obj = datetime.datetime.strptime(date_time_str, '%d.%m.%Y')
    #     print('Дата:', date_time_obj.date())
    #     # print(r.text)

    # for i in platforms:
    #     print(i.text)

