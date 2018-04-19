import string
from bin_hex_converter import hex_to_bin
import encoder
import decoder
import unittest


class EncodingDecodingTest(unittest.TestCase):
    def test_nrz_i(self):
        print('NRZ-I')
        self.all_combinations_in_2_bytes(technique='nrz_i')

    def test_manchester(self):
        print('MANCHESTER')
        self.all_combinations_in_2_bytes(technique='manchester')

    def all_combinations_in_2_bytes(self, technique='nrz_i'):
        hex_digits = sorted(set(string.hexdigits.upper()))  # list of hexa digits
        for hex0 in hex_digits:
            for hex1 in hex_digits:
                for hex2 in hex_digits:
                    for hex3 in hex_digits:
                        hex_string = hex0 + hex1 + hex2 + hex3
                        print('0x%s' % hex_string)
                        bin_string = hex_to_bin(hex_string)

                        if technique == 'nrz_i':
                            encoded_bin_string = encoder.nrz_i(bin_string)
                            decoded_signal_string = decoder.nrz_i(encoded_bin_string)
                        elif technique == 'manchester':
                            encoded_bin_string = encoder.manchester(bin_string)
                            decoded_signal_string = decoder.manchester(encoded_bin_string)
                        else:
                            raise Exception('Technique %s not implemented' % technique)

                        self.assertEquals(decoded_signal_string, bin_string, msg='Decoded signal isn\'t equal to original binary sequence')


if __name__ == '__main__':
    unittest.main()
