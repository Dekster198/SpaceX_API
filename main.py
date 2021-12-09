import requests, datetime
from tkinter import *

window = Tk()
window.geometry('800x600+200+100')
window.title('SpaceX API')
window.mainloop()

class Launches:
    def getNextLaunch(self):
        endpoint = 'https://api.spacexdata.com/v3/launches/next'
        response = requests.get(endpoint)
        data = response.json()
        timestamp = datetime.datetime.fromtimestamp(data['launch_date_unix'])
        text = 'Миссия: ' + data['mission_name'] + '\nДата запуска: ' + timestamp.strftime('%Y-%m-%d %H:%M:%S')
        lbl = Label(window, text = text)
        lbl.grid(column=0, row=0)
        window.mainloop()


class Rockets():
    def getRockets(self):
        endpoint = 'https://api.spacexdata.com/v3/rockets'
        response = requests.get(endpoint)
        data = response.json()
        for d in data:
            print('Наименование ракеты: ' + d['rocket_name'] + '\n' + d['wikipedia'] + '\n', 'Масса ракеты:',
                  d['mass']['kg'], '\n',
                  'Описание:', d['description'], '\n', 'Ссылки на изображения:', d['flickr_images'][:])
            print('\n')

class SpaceShips():
    def getSpaceShips(self):
        endpoint = 'https://api.spacexdata.com/v3/dragons'
        response = requests.get(endpoint)
        data = response.json()
        for d in data:
            print('Наименование космического корабля:', d['name'], '\n', d['wikipedia'], '\n', 'Описание:',
                  d['description'], '\n', 'Изображения: ', d['flickr_images'][:])
            print('\n')

change = int(input('Выберите тип: 1 - Ракета; 2 - Космический корабль: '))
if(change == 1):
    rockets = Rockets()
    rockets.getRockets()
elif(change == 2):
    spaceShips = SpaceShips()
    spaceShips.getSpaceShips()