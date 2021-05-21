import time
import json
import requests
from omegaconf import OmegaConf


TOKEN = OmegaConf.load("tokens/autocheck_bot.yaml").TOKEN
URL = "https://api.telegram.org/bot"
TEXT = "Не знаю, какое-нибудь"
UPDATE_ID_FILE = "metainfo/update.txt"


def main(): ## fgffg
    update_id = 0
    while True:
        # Get new messages to out bot
        updates = requests.get(f"{URL}{TOKEN}/getUpdates?offset={update_id}").json()["result"]
        # print(updates)
        # processing new messages
        for update in updates:
            if update["update_id"] >= update_id:
                update_id = update["update_id"] + 1

            chat_id = update["message"]["chat"]["id"]
            # send message to chat id
            send = requests.post(f"{URL}{TOKEN}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={TEXT}")
        time.sleep(5)


if __name__ == "__main__":
    main()


