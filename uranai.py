import random

def number_input(message):
    result = input(message)
    if(result.isdigit()):
        result = int(result)
        return result
    else:
        return 0

def judgement(omikuji):
    rand = random.randint(1,9)
    if (omikuji == rand):
        print('大吉ですね')
    elif(omikuji > rand):
        print('中吉ですね')
    elif(omikuji < rand):
        print('凶ですね...')

while(True):
    omikuji = number_input('1~9で好きな数字を入力してください。\n\n')
    if((omikuji !=0) and (omikuji > 0) and (omikuji < 10)):
        print('あなたの好きな数字は' + str(omikuji) + 'ですね！\n\n')
        print('それではその数字からあなたの命運を占いましょう\n\n')

        judgement(omikuji)
        break
    else:
        print('1~9の数字を入力してください。\n\n')
