from payyans import Payyans


def payyans_unicode2ascii(text, font):
    P = Payyans()
    return P.Unicode2ASCII(text, font)


def payyans_ascii2unicode(text, font):
    P = Payyans()
    return P.ASCII2Unicode(text, font)


def ascii2unicode():
    return [payyans_ascii2unicode, str, str, str]


def unicode2ascii():
    return [payyans_unicode2ascii, str, str, str]
