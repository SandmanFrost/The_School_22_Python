import re

pat = r"spam"
# совпадение в начале строки(re.match(*,"*"))
if re.match(pat, "eggspamsousagespam"):
    print("+")
else:
    print("-")
# Совпадение во всей строке(при первом совпадении выведет "+")
if re.search(pat, "eggspamsousagespam"):
    print("+")
else:
    print("-")
# Все совпадения в строке вывод
print(re.findall(pat, "eggspamsousagespam"))
# Группы совпадений
pat = r"ggs"
match = re.search(pat, "eggspamsousage")
if match:
    # Возвращает совпавшую строку
    print(match.group())
    # Возвращает начальную позицию совпадения(e-0,g-1,g-2,s-3,p-4,a-5,m-6,s-7,o-8,u-9,s-10,a-11,g-12,e-13)
    print(match.start())
    # Возвращает последнюю позицию совпадения
    print(match.end())
    # Возвращает начальную и последнюю позицию совпадения
    print(match.span())

# поиск и замена слова (pattern) в str, и заменяет его на re.sub(что менять, на что менять, где менять, сколько менять) 
print("\nПоиск и замена символа(-ов) в строке")
str = "Hello, my name is Joch. Welcome Joch."
pattern = r" "
newstr = re.sub(pattern, "-", str, count=0)
print(newstr)

# Метасимволы
print("\nМетасимволы:")
print("Метасимвол . :")
# . - матасимвол означает любой символ кроме новой строки
pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("grey +")
else:
    print("grey -")
if re.match(pattern, "gray"):
    print("gray +")
else:
    print("gray -")
if re.match(pattern, "blue"):
    print("blue +")
else:
    print("blue -")

# ^ - метасимвол указывает на начало строки
# $ - метасимвол указывает на конец строки
print("\nМетасимволы ^ и $ :")
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("grey +")
else:
    print("grey -")
if re.match(pattern, "gray"):
    print("gray +")
else:
    print("gray -")
if re.match(pattern, "stringrey"):
    print("stringrey +")
else:
    print("stringrey -")

# Классы символов
print("\nКлассы символов:")
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
    print("grey +")
else:
    print("grey -")
if re.search(pattern, "qwertyuiop"):
    print("qwertyuiop +")
else:
    print("qwertyuiop -")
if re.search(pattern, "rhythm myths"):
    print("rhythm myths +")
else:
    print("rhythm myths -")

# В диапозоне
print("\nПоиск классов в диапозоне символов в строке([a-z],[A-Z],[0-9],[a-zA-Z])")
pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS8"):
    print("LS8 +")
else:
    print("LS8 -")
if re.search(pattern, "E3FF1"):
    print("E3FF1 +")
else:
    print("E3FF1 -")
if re.search(pattern, "1ab"):
    print("1ab +")
else:
    print("1ab -")

# Инвертация
print("\nИнвертация([^a-z],[^A-Z],[^0-9],[^a-zA-Z])")
pattern = r"[^A-Z]"
if re.search(pattern, "LS"):
    print("LS +")
else:
    print("LS -")
if re.search(pattern, "E3"):
    print("E3 +")
else:
    print("E3 -")
if re.search(pattern, "1ab"):
    print("1ab +")
else:
    print("1ab -")
