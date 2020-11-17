UTF_MODE = 'utf-8'


def to_unicode(usr_input: str):
    '''
    Convert string to utf-8 encoded bytes
    :param usr_input: string from program
    :return: UTF-8 bytes
    '''
    return usr_input.encode(UTF_MODE)


def to_text(utf_str: bytes):
    '''
    Convert utf-8 to string
    :param utf_str: UTF-8 bytes
    :return: String
    '''
    return utf_str.decode(UTF_MODE)


def to_list(utf_str: bytes):
    '''
    Use list to break down character from unicode
    :param utf_str: UTF-8 bytes
    :return: List from bytearray
    '''
    utf_list = bytearray(utf_str)
    return list(utf_list)
