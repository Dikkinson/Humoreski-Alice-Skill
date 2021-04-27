from telethon import TelegramClient

import json

# Remember to use your own values from my.telegram.org!
api_id = 132911
api_hash = '33bdf82a3461923675cf74ddf682329d'
client = TelegramClient('serega', api_id, api_hash)


async def main():
    umorezki = []
    # You can print the message history of any chat:
    async for message in client.iter_messages(-1001143742161):
        if not message.photo and not message.entities:
            if len(str(message.text)) < 1024:
                umorezki.append(message.text)
    with open('umorezki.txt', 'w', encoding="utf-8") as outfile:
        json.dump(umorezki, outfile, ensure_ascii=False)


with client:
    client.loop.run_until_complete(main())
