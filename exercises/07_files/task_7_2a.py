#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
with open(argv[1], 'r') as f:
    for line in f:
        ignore_line = True in [word in line for word in ignore]
        if not line.startswith('!') and not ignore_line:
            print(line.rstrip())