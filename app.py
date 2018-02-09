import requests

import messageHandler
import vk_api
import setting

from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType

def main():
    session = requests.Session()

    # Авторизация пользователя:
    """
    login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    """

    # Авторизация группы:
    # при передаче token вызывать vk_session.auth не нужно

    vk_session = vk_api.VkApi(token=setting.token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session, 2)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
            print(event.attachments)
            # message = 'Сам ' + event.text
            # attachments = []
            msg = messageHandler.get_answer(event)

            vk.messages.send(
                user_id=event.user_id,
                attachment=msg[1],
                message=msg[0]
            )
            print('ok')        
            
if __name__ == '__main__':
    main()