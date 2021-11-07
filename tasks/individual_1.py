#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
На вход программы поступает строка из целых чисел, записанных через пробел. Напишите
функцию get_list , которая преобразовывает эту строку в список из целых чисел и
возвращает его. Определите декоратор для этой функции, который сортирует список чисел,
полученный из вызываемой в нем функции. Результат сортировки должен возвращаться при
вызове декоратора. Вызовите декорированную функцию get_list и отобразите полученный
отсортированный список на экране.
"""


def decorate_function(func):
    def wrapper(*args):
        if args:
            values = [int(arg) for arg in args]
            values.sort()
            func(values)
    return wrapper


@decorate_function
def get_list(args):
    print(args)


if __name__ == '__main__':
    get_list(*list(map(int, input('Введите список через пробел: ').split(' '))))
