#Задание №1 «Input validation»
# Вам нужно сделать валидацию входных 
# данных (Input validation) для умножения 
# данных в заявке-заказе
# x = int(input('1st factor <= 10 digit number: '))
# y = int(input('2nd factor <= 10 digit number: '))
# print('Total = ', x*y)

#Задание №1 (ответ*)
# x = input('1st factor <= 10 digit number: ')
# y = input('2nd factor <= 10 digit number: ')
# while (len(x) > 10 or (not x.isdigit())) or (len(y) > 10 or (not y.isdigit())):
#     print('There is no 10 digit number')
#     x = input('1st factor <= 10 digit number: ')
#     y = input('2st factor <= 10 digit number: ')
# x = int(x)
# y = int(y)
# print('Total = ', x*y)

#Задание №2 «Input validation»
# Вам нужно сделать валидацию входных данных (Input validation) и санитизацию выходных данных 
# (Sanitize) в команды к операционной системе при создании каталогов для хранения материалов заявок-
# заказов
#Ввести 
# 1. D:\\_WORK\\TEST
# 2. D:\\_WORK\\test1 & %windir%\\system32\\nodepad.exe
# import os
# input_path = input('Catalogue path:')
# command = f'mkdir {input_path}'
# os.popen(command)

#Задание №2 (ответ*)
# import os
# input_path = input('Catalogue path:')
# spec_symbols = ['*', '?', '<', '>', '&', '|', '&']
# check = [characters in input_path for characters in spec_symbols]
# while True in check:
#     for i in range(len(check)):
#         check[i] = False
#     print('Incorrect catalogue path')
#     check = [characters in input_path for characters in spec_symbols]
# command = f'mkdir {input_path}'
# os.popen(command)
# print('Catalogue was successfuly created')

#Задание №3 «Input validation»
# Вам нужно сделать валидацию входных данных (Input validation) для блока с выполнением 
# произвольного кода*
# compute_user_input = input('\nFactors and operator computing: ')
# if not compute_user_input:
#     print("No input")
# else:
#     print("Result: ", eval(compute_user_input))

#Задание №3 (ответ*)
# compute_user_input = input('\nFactors and operator computing: ')
# if not compute_user_input:
#     print("No input")
# else:
#     print("Result: ", eval(compute_user_input, {'__builtins__':{}}))
    
#Задание №4 «Output encoding»
# Вам нужно сделать унифицированное 
# преобразование выходных данных 
# (Output encoding)
# Name_input = input('\nFirst and last name: ')
# print(f'Your data: {Name_input}')

#Задание №4 (ответ*)
# Name_input = input('\nFirst and last name: ')
# print(f'Your data: {Name_input.title()}')
# print(f'Your data: {Name_input.upper()}')
# print(f'Your data: {Name_input.lower()}')

#Задание №5 «Error handling and logging»
# import os
# import logging
# import datetime

# logging.basicConfig(level=logging.DEBUG, filename='test_log.log', filemode='w')

# input_path = input('Catalogue path: ')
# spec_symbols = ['*', '?', '<', '>', '&', '|', '&']
# check = [characters in input_path for characters in spec_symbols]
# while True in check:
#     for i in range(len(check)):
#         check[i] = False
#     logging.info(f'{datetime.datetime.now()} Suspicious value: {input_path}')
#     print('Incorrect catalogue path')
#     input_path = input('Catalogue path: ')
#     check = [characters in input_path for characters in spec_symbols]
# command = f'mkdir {input_path}'
# os.popen(command)
# print('Catalogue was succefully created')

#Задание №6 «Authentication and password management»
# Вам нужно безопасно сохранить пароли пользователей (Authentication and password management)

# dict_users = {'user1': 'password1', 'user2': 'passowrd2'}
# print(dict_users)

#Задание №6 (ответ*)
#1
import hashlib
dict_users = {'user1': 'password1', 'user2': 'passowrd2'}
for i in dict_users:
    dict_users[i] = hashlib.sha256(dict_users[i].encode()).hexdigest()
print(dict_users)
#2
import bcrypt
dict_users = {'user1': 'password1', 'user2': 'passowrd2'}
for i in dict_users:
    dict_users[i] = bcrypt.hashpw(dict_users[i].encode(),bcrypt.gensalt())
print(dict_users)