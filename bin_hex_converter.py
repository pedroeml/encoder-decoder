

def hex_to_bin(hex_string):
    return ''.join('{0:04b}'.format(int(c, 16)) for c in hex_string)

