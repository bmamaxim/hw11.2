#Функции работы с текстом
def str_upper(word: str):
    """
    Возвращает слово в верхнем регистре
    :param word: str
    :return: str
    """
    return word.upper()


def get_title(words: str) -> str:
    """
    Каждое новое слово с большой буквы
    :param words: str
    :return: str
    """
    return words.title()
