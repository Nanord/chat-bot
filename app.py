import messageHandler
import vk_api
import setting

from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType

def main():
    vk_session = vk_api.VkApi(token=setting.token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session, 2)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            # message = '       ' + event.text
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
