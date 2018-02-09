import vk
import requests
import datetime

session = vk.Session()
api = vk.API(session, v=5.0)

def userName(id, case):
	profiles = api.users.get(user_id=id, name_case=case)
	return profiles[0]['first_name']

def getStatus(id):
    profiles = api.users.get(user_id=id, fields='online, last_seen')
    if (profiles[0]['online']):  # если появился в сети, то выводим время
        now = datetime.datetime.now()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Появился в сети в: ', now.strftime("%d-%m-%Y %H:%M"))
        return 'Появился в сети в: ' + now.strftime("%d-%m-%Y %H:%M")
    if (current_status) and (not profiles[0]['online']):  # если был онлайн, но уже вышел, то выводим время выхода
        print('Вышел из сети: ', datetime.datetime.fromtimestamp(profiles[0]['last_seen']['time']).strftime('%d-%m-%Y %H:%M'))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return 'Вышел из сети: ' + datetime.datetime.fromtimestamp(profiles[0]['last_seen']['time']).strftime('%d-%m-%Y %H:%M') 

# def uploadPhoto(id_photo)
# 	url_photo = api.photos.getMessagesUploadServer(peer_id=id_photo)
# 	response = session.get(
# 		url_photo.upload_url
# 		).json()
# 	photo = api.photos.getMessagesUploadServer()