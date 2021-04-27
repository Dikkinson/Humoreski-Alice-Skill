from telethon import TelegramClient, events, sync

api_id = 132911
api_hash = '33bdf82a3461923675cf74ddf682329d'

client = TelegramClient('serega', api_id, api_hash)
client.start()

messages = client.get_messages(-1001143742161, 20)
for message in messages:
    if not message.photo and not message.entities:
        print(message.text)
        break
