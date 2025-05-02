# Урок 10. Семинар: Безопасная разработка приложений
# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.
import hashlib
password = input('Введите пароль (длина должна быть не менее 8 символов, с прописными и строчными буквами, а также с цифрами): ')
while (len(password) < 8 or not(any(char.isupper() for char in password)) or not(any(char.isdigit() for char in password)) or not(any(char.islower() for char in password))):
    print('Пароль должен быть длиной не менее 8 символов, содержать прописные и строчные буквы, а также цифры')
    password = input('Введите пароль длиной не менее 8 символов, с прописными и строчными буквами, а также с цифрами: ')
password = hashlib.sha256(password.encode()).hexdigest()
print(password)