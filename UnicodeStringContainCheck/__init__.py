from . import utf_iostream as utfio


def utf_contain(usr_input: str, target_text: str):
    '''
    Design for oriental text system that to find out does words contained in string
    :param usr_input: Input
    :param target_text: Target word parameter
    :return: Does target word contains or not
    '''
    if len(target_text) > len(usr_input):
        raise IndexError("Target word's length should be smaller than the input")
    input_utf_bin = utfio.to_list(utfio.to_unicode(usr_input))
    target = utfio.to_list(utfio.to_unicode(target_text))
    target_size = len(target)
    matched_word_buffer = []
    finding_col = 0
    for i in input_utf_bin:
        if i == target[finding_col]:
            # Add buffer when find out is contain
            matched_word_buffer.append(target[finding_col])
            finding_col += 1
            if finding_col == target_size:
                # Return true when found the word
                return True
        else:
            # Reset to ensure the words is stick together
            matched_word_buffer.clear()
            finding_col = 0

    return False
