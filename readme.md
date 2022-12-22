Звіт до комп’ютерного проєкту “Аналог бібліотеки itertools”

Структура проєкту:
    1. count()
    2. cycle()
    3. repeat()
    4. product()
    5. permutations()
    6. combinations()
    7. combinations_with_replacement()
    8. модуль для тестування

ОПИС АЛГОРИТМІВ:

count()
Функція повертає ітератор нескінченного циклу по цілих числах, опціональний аргумент - step, якщо вказаний - то крок множиться на step. Наприклад, при виклику функції count(10, 2), next(count(10, 2)) == 10, 12, 14 і так далі. Якщо число не ціле, або аргумент не інтовий, то викликається AssertionError.

cycle()
Функція повертає нескінченний ітератор по циклу вмісту ітератора. Якщо об’єкт не ітерований, то викликається AssertionError. При виклику cycle([10, 20, 30]), next(cycle([10, 20, 30])) == 10, 20, 30, 10, 20, 30 і так далі.

repeat()
Функція повертає нескінченний ітератор повторюваних значень. При виклику repeat(10), next(repeat(10)) == 10, 10, 10 і так далі.

product(*args, **kwds)
Функція приймає два аргументи: об'єкт/-и, з яких створюють перестановки, і кількість повторів в елементів в результаті. Повертає множину декардового добутку.
Функція recursive є підфункією, яка є генератором і генерує кортеж з елементів, переданих в першому аргументі.
Приклад вводу: 'ABCD', 'xy' 
Приклад виводу: [('А', 'х'), ('А', 'у'), ('В', 'х'), ('С', 'х'), ('С', 'у'), ('D', 'x'), ('D', 'y')]
Першим елементом кортежу є елемент з першого списку, другим – другий, і так далі
Використані знання з дискретної математики: поняття множини, поняття елементів множини, декардового добутку

permutations(iterable: str | list | tuple, length: int)
Функція приймає два аргументи: об’єкт, з якого складають перестановки, і довжину перестановки. Функція створює ітератор усіх можливих перестановок. Наприклад, якщо ввести список  [1, 2, 3], ітератор по черзі поверне наступні перестановки: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1). Якщо вказано довжину перестановки, то функція повертатиме перестановки даної довжини.
Алгоритм функції полягає в тому, що створюються два списки: indices (індекси всіх елементів перестановки) і cycles (довжина цього списку буде дорівнювати дорівнювати даній у функції довжині). Для прикладу, наведеному вище, ці списки будуть такі:
indices= [0, 1, 2]
cycles = [3, 2, 1]
Наступним кроком є цикл, який генерує всі перестановки, використовуючи створені попередньо списки. Спочатку закріплюється перший елемент і переставляються всі наступні, потім другий елемент стає на перше місце і переставляються всі інші і так далі.
Використані знання з дискретної математики: поняття множини, перестановки елементів множини.

combinations(iterable: str | list | tuple, length: int) 
str | list | tuple, int→ iterator
Функція приймає два аргументи: елементи, з яких будуть складаних комбінації та бажана кількість елементів у комбінації, та повертає усі можливі комбінації без повторень заданої довжини довжини. Наприклад:
combinations('ABCD', 2) --> AB AC AD BC BD CD
	Структура функції складається з трьох частин: перевірка вхідних даних, генерування першої комбінації та генерування наступних комбінацій. 
	Перша комбінація складається із елементів з перших length індексів. Далі функція Працює за допомогою циклу while, в якому щоразу збільшує останній ідекс в комбінації на одиницю.
Використані знання з дискретки: комбінації елементів множини  без повторень

combinations_with_replacement()
Функція так само, як і combinations() приймає два аргументи: елементи, з яких будуть складаних комбінації та бажана кількість елементів у комбінації, та повертає генератор усіх можливих комбінацій з повтореннями.
combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
Принцип роботи доволі простий. Функція зроблена на основі product, яка повертає декартів добуток елементів. Все що залишається це позабирати обернені значення.


ПРОЦЕС ВИКОНАННЯ
Виконання проекту складалось з кількох етапів:
Найперше це була зустріч команди, на якій було обрану тему даного проекту та розподілено обов’язки ( вони описані у пункті “Команда та розподіл роботи”).
Після цього кожен приступив до написання своєї частини. Цей етап роботи включав в себе придумання алгоритму для функції та втілення його у код. Далі самостійне тестування коду та перевірка на відповідність до вимог PEP8. Також на цьому етапі відбулась проміжна зустріч команди, де кожен задавав питання щодо завдань або просив поради щодо виконання якогось із завдань, а інша частина команди допомагала із вирішенням озвучених проблем.
Тестування функцій за допомогою написаного модуля.
На третій зустрічі команди кожен із учасників прийшов із готовими функціями і презентував її перед рештою команди. Інші учасники могли задавати питання і висловлювати поради. Після презентації кожен завантажив свою частину завдання на GitHub.
Створення презентації проекту
Написання звіту
Команда та розподіл роботи
Проєкт виконала команда №10, а саме:

Саворона Костятин - count(), cycle(), repeat(), модуль для тестування
Гнип Олена - permutations(), оформлення презентації
Савчин Юлія - product()
Куц Христина - combinations(), написання звіту
Шарак Святослав-Микола - combinations_with_replacement()


Відгуки
“Виконання проекту сподобалось, цікаво втілювати в код знання з дискретної математики. Для реалізації власних алгоритмів бракувало знань про дерева та backtracking, а також бракувало загальних знань про ефективність тих чи інших алгоритмів. Лекція з ОП та цю тему була в самому кінці виконання даного проекту” - Христина Куц.

“Було цікаво працювати в команді над написанням коду. Вивчила застосування бібліотеки itertools та дослідила різні аналоги функцій цієї бібліотеки. Дуже допомогли в реалізації коду знання з дискретної математики щодо множин. Загалом було дуже пізнавально” - Олена Гнип.





