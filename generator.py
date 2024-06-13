import random


def passGenerator(number):
    words = ["elu", "aabits", "kodu", "õun", "koer", "kass", "raamat", "õnn", "armastus", "sõprus", "pere", "töö", "mäng", "õis", "lill",  "rõõm", "kurbus", "õhtu", "hommik", "päev", "öö", "linn", "mets", "meri", "jõgi", "mägi", "tänav", "kool", "õpik", "pliiats", "paber", "arvuti", "telefon", "teler", "raadio", "muusika", "sport", "jooks", "hüpe", "ujumine", "jalgratas", "auto", "buss", "rong", "lennuk", "laev", "kaart", "pilt", "foto", "laul", "kuusk", "mänd", "kajakas", "tuvi", "roos", "ümbrik", "vihik", "kaktus", "ülane", "vetikas", "ankur", "ookean", "austama", "kirss", "ploom", "esinema", "hammas", "äike", "päike", "kutsikas", "jänes", "põder"]
    selected_word = []

    number = max(min(number, 10), 1)

    for nr in range(number):
        word = random.choice(words)
        selected_word.append(word)
        words.remove(word)

    return '-'.join(selected_word)


def addNumbers(number, passphrase):
    words = passphrase.split("-")
    number_count = max(min(number, len(words)), 0)

    if number_count == 0:
        return passphrase

    words_with_numbers = []

    for _ in range(number_count):
        rand_word_index = random.randint(0, len(words)-1)
        rand_word = words.pop(rand_word_index)
        rand_word += str(random.randint(0, 9))

        words_with_numbers.append(rand_word)

    words_with_numbers += words

    random.shuffle(words_with_numbers)

    return "-".join(words_with_numbers)


def toUpper(passphrase):
    return passphrase.title()
