# Проект DialogBot

Данные проект позволяет добавлять нейросеть с ответами в ваши боты, используя [dialogflow](https://cloud.google.com/dialogflow?hl=ru)


## Запуск

Для запуска скрипта, Вам нужен Python не ниже версии 3.

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл .env и добавьте в него необходимые переменные окружения
- Запустите файл со скриптом для vk `vk.py`
- Запустите файл со скриптом для tg `bot.py`

## Переменные окружения

Для работы скрипта, нужно создать файл `.env` в одной папке с файлом `main.py` и записать туда данные в
таком формате: `ПЕРЕМЕННАЯ=значение`.


Необходимы следующие переменные:
- `TG_BOT_TOKEN` - Токен вашего бота TG. Как создать [бота](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot)
- `TG_USER_ID` - ID вашего чата в ТГ, для получения [напишите](https://t.me/userinfobot)
- `DIALOG_TOKEN` - Ваш токен в DialogFlow
- `GOOGLE_APPLICATION_CREDENTIALS` - укажите путь к файлу applications_default_credentials.json, он располагается внутри папки
- `PROJECT_ID` - id вашего проекта в Dialogflow
- `VK_GROUP_TOKEN` - токен от вашей группы вк

## Пример работы

Проверить работоспособность можно в ТГ [боте](https://t.me/devman_publishingBot) и в группе [вк](https://vk.com/club225711224)
![test](https://github.com/trader-daniil/publishing/assets/74257219/0ca674d6-aa61-408a-b3ed-c1346953256a)


