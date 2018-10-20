#!/usr/bin/env python
# encoding: utf-8

import math
import random

NumberRange = [0,1024]
history = dict()

def try_to_guess(name, answer):
    try_num = 0
    max_num = math.log2(NumberRange[0] + NumberRange[1])

    while try_num < max_num:
        guess_answer = int(input('please input a number: '))
        if guess_answer < answer:
            print('The number you input is samller than answer')
        elif guess_answer == answer:
            print('Correct!')
            history[name].append('Success')
            break
        else:
            print('The number you input is bigger than answer')

        try_num += 1
    else:
        print('Guess error too many times.Failure!')
        history[name].append('Failure')

def get_number_range(split_char=' '):
    input_string = input('Please input the number range to guess splited by "{}".Default is 0~1024: '.format(split_char))
    num_min, num_max = input_string.split(split_char)
    return int(num_min), int(num_max)

def get_user_name():
    username = input('Please input the username: ')
    return username

def get_option():
    print("1. history record")
    print("2. continue")
    print("3. exit")
    return int(input('Choose your option: '))

def show_user_history(name):
    print('User: {}, record: {}'.format(name,history[name]))

def game_start():
    name = get_user_name()
    NumberRange[0], NumberRange[1] = get_number_range()

    history[name] = list()

    option = int()
    while True:
        try_to_guess(name, random.randint(NumberRange[0],NumberRange[1]))
        option = get_option()
        while option == 1:
            show_user_history(name)
            option = get_option()
        if(option == 2):
            continue
        elif(option == 3):
            exit()

if __name__ == '__main__':
    game_start()
