import random
from config import symbols, ascii


def createAsciiTable():
    "Нормализация таблицы символов"
    ascii["а"] = ascii["а"][random.randint(0, len(ascii["а"])-1)]
    ascii["ж"] = ascii["ж"][random.randint(0, len(ascii["ж"])-1)]
    ascii["л"] = ascii["л"][random.randint(0, len(ascii["л"])-1)]
    ascii["ф"] = ascii["ф"][random.randint(0, len(ascii["ф"])-1)]
    ascii["х"] = ascii["х"][random.randint(0, len(ascii["х"])-1)]
    ascii["ш"] = ascii["ш"][random.randint(0, len(ascii["ш"])-1)]
    ascii["ы"] = ascii["ы"][random.randint(0, len(ascii["ы"])-1)]
    ascii["я"] = ascii["я"][random.randint(0, len(ascii["я"])-1)]


def welcomeText():
    print("""========== ASCII Конвертер Никнеймов ==========
Версия: 0.1
Автор: MOHOVICK
          
Данная программа преобразует ваш никнейм в старом стиле.
Например, если ваш ник "Кот в сапогах", то после конвертации вы получите "K0T_B_C@/70r@X" уже на латинице

Иногда при генерации некоторые буквы (такие как "a", "ж", "л", "ф", "x", "ш", "ы", "я")
могут иметь разные ASCII символы, так как их можно представить разными ASCII символами

Все вводимые слова(никнеймы) должны быть исключительно на русском языке, иначе ничего не получится...
""")
    input("Нажмите Enter для продолжения...")


if __name__ == "__main__":
    welcomeText()
    nickname = list(input("Введите никнейм: ").casefold())
    if not nickname:
        print("[INFO] Пустой текст...")

    createAsciiTable()
    ascii_nickname = []
    for i in nickname:
        for x in symbols:
            if i == x:
                ascii_nickname.append(ascii[i])

    new_nickname = "".join(ascii_nickname)
    print(f"Ваш новый никнейм: {new_nickname}")
