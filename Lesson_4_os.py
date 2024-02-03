import os
import webbrowser

while True:
    web_page = input("Введите адрес сайта: ")

    if web_page == "stop":
        break

    if 'https://' in web_page:
        os.system('open ' + web_page)
        print('if')
    elif 'www.' in web_page:
        web_page = 'https://' + web_page
        os.system('open ' + web_page)
        print('elif')
    else:
        web_page = 'https://www.' + web_page
        os.system('open ' + web_page)
        print('else')