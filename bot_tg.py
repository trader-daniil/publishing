from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from dotenv import load_dotenv
from dialog import detect_intent_texts


from functools import partial


LANGUAGE_CODE = 'ru'


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!",
    )


def get_response_from_dialog_flow(update, context, project_id, tg_user_id):
    recieved_message = update.message.text
    dialog_flow_response = detect_intent_texts(
        project_id=project_id,
        session_id=tg_user_id,
        texts=(recieved_message,),
        language_code=LANGUAGE_CODE,
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=dialog_flow_response['fulfillment_text'],
    )


def main():
    load_dotenv()
    tg_token = os.getenv('TG_BOT_TOKEN')
    project_id = os.getenv('PROJECT_ID')
    tg_user_id = os.getenv('TG_USER_ID')
    updater = Updater(
        token=tg_token,
        use_context=True,
    )
    dispatcher = updater.dispatcher
    start_handler = CommandHandler(
        'start',
        start,
    )
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(
        Filters.text & (~Filters.command),
        partial(
            get_response_from_dialog_flow,
            project_id=project_id,
            tg_user_id=tg_user_id,
        )
    )
    dispatcher.add_handler(echo_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()
