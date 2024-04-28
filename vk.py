import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from dialog import detect_intent_texts
from dotenv import load_dotenv
import os
import vk_api as vk


load_dotenv()

LANGUAGE_CODE = 'ru'


def echo(event, vk_api):
    project_id = os.getenv('PROJECT_ID')
    tg_user_id = os.getenv('TG_USER_ID')
    dialog_response = detect_intent_texts(
        project_id=project_id,
        session_id=tg_user_id,
        texts=(event.text,),
        language_code=LANGUAGE_CODE,
    )
    if dialog_response:
        vk_api.messages.send(
            user_id=event.user_id,
            message=dialog_response,
            random_id=random.randint(1,1000)
        )

if __name__ == "__main__":
    vk_token = os.getenv('VK_GROUP_TOKEN')
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)
