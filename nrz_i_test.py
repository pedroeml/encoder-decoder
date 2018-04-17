from bin_hex_converter import hex_to_bin
import encoder
import decoder
import unittest


class TestNrz_i(unittest.TestCase):
    def test_all_combinations_in_2_bytes(self):
        all_hexa = '123456789ABCDEF'
        for c0 in all_hexa:
            for c1 in all_hexa:
                for c2 in all_hexa:
                    for c3 in all_hexa:
                        hex_string = c0 + c1 + c2 + c3
                        print('0x%s' % hex_string)
                        bin_string = hex_to_bin(hex_string)
                        encoded_bin_string = encoder.nrz_i(bin_string)
                        print(bin_string)
                        print(encoded_bin_string)
                        decoded_signal_string = decoder.nrz_i(encoded_bin_string)
                        print(decoded_signal_string)
                        self.assertEquals(decoded_signal_string, bin_string, msg='Decoded signal isn\'t equal to original binary sequence')


if __name__ == '__main__':
    unittest.main()
