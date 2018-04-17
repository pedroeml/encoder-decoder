import string
from bin_hex_converter import hex_to_bin
import encoder
import decoder
import unittest


class TestNrz_i(unittest.TestCase):
    def test_all_combinations_in_2_bytes(self):
        hex_digits = ''.join(sorted(set(string.hexdigits.upper())))
        for hex0 in hex_digits:
            for hex1 in hex_digits:
                for hex2 in hex_digits:
                    for hex3 in hex_digits:
                        hex_string = hex0 + hex1 + hex2 + hex3
                        print('0x%s' % hex_string)
                        bin_string = hex_to_bin(hex_string)
                        encoded_bin_string = encoder.nrz_i(bin_string)
                        print(bin_string)
                        print(encoded_bin_string)
                        decoded_signal_string = decoder.nrz_i(encoded_bin_string)
                        self.assertEquals(decoded_signal_string, bin_string, msg='Decoded signal isn\'t equal to original binary sequence')


if __name__ == '__main__':
    unittest.main()
