

def hex_to_bin(hex_string):
    """
    Converts a string containing hexadecimal digits to a string containing binary digits.

    :param hex_string:
    :type hex_string: str
    :return:
    :rtype: str
    """
    return ''.join('{0:04b}'.format(int(c, 16)) for c in hex_string)

