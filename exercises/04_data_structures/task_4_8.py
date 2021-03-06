# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1'
IP = IP.split('.')
a = int(IP[0])
b = int(IP[1])
c = int(IP[2])
d = int(IP[3])
ip_template = '''
         {0:<10} {1:<10} {2:<10} {3:<10}
         {0:010b} {1:010b} {2:010b} {3:010b}
         '''
print(ip_template.format(a, b, c, d))