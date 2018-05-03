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

    def test_mlt3(self):
        print('MLT-3')
        self.all_combinations_in_2_bytes(technique='mlt-3')

    def test_8b10b(self):
        print('8B10B')
        self.all_combinations_in_2_bytes(technique='8b10b')

    def test_techniques(self):
        hex_strings = ['5265646573', '436f6d70757461646f72', '6e727a69', '6d616e63686573746572', '6d6c7433', '3862313062']

        for hex_string in hex_strings:
            print('0x%s' % hex_string)
            bin_string = hex_to_bin(hex_string)

            encoded_bin_string = encoder.nrz_i(bin_string)
            decoded_signal_string = decoder.nrz_i(encoded_bin_string)
            self.assertEqual(decoded_signal_string, bin_string, msg='NRZ-I: Decoded signal isn\'t equal to original binary sequence')

            encoded_bin_string = encoder.manchester(bin_string)
            decoded_signal_string = decoder.manchester(encoded_bin_string)
            self.assertEqual(decoded_signal_string, bin_string, msg='Manchester: Decoded signal isn\'t equal to original binary sequence')

            encoded_bin_string = encoder.mlt3(bin_string)
            decoded_signal_string = decoder.mlt3(encoded_bin_string)
            self.assertEqual(decoded_signal_string, bin_string, msg='MLT-3: Decoded signal isn\'t equal to original binary sequence')

            encoded_bin_string, bits_10b_string = encoder.to8b10b(bin_string)
            bin_string = bits_10b_string
            decoded_signal_string = decoder.nrz_i(encoded_bin_string)
            self.assertEqual(decoded_signal_string, bin_string, msg='8B10B: Decoded signal isn\'t equal to original binary sequence')

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
                        elif technique == 'mlt-3':
                            encoded_bin_string = encoder.mlt3(bin_string)
                            decoded_signal_string = decoder.mlt3(encoded_bin_string)
                        elif technique == '8b10b':
                            encoded_bin_string, bits_10b_string = encoder.to8b10b(bin_string)
                            bin_string = bits_10b_string
                            decoded_signal_string = decoder.nrz_i(encoded_bin_string)
                        else:
                            raise Exception('Technique %s not implemented' % technique)

                        self.assertEqual(decoded_signal_string, bin_string, msg='Decoded signal isn\'t equal to original binary sequence')


if __name__ == '__main__':
    unittest.main()
