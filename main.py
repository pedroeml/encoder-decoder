from bin_hex_converter import hex_to_bin
import encoder
import decoder

if __name__ == '__main__':
    finish = False

    while not finish:
        encode_decode = input('Encode or decode? ')

        if encode_decode.lower() not in ['encode', 'decode']:
            finish = True
            continue

        technique = input('NRZ-I, Manchester, MLT-3 or 8B10B? ')

        if technique.lower() not in ['nrz-i', 'manchester', 'mlt-3', '8b10b']:
            continue

        if encode_decode == 'encode':
            hex_string = input('Hex: 0x')

            bin_string = hex_to_bin(hex_string)

            print('Bin: %s' % bin_string)

            if technique == 'nrz-i':
                print(encoder.nrz_i(bin_string))
            elif technique == 'manchester':
                print(encoder.manchester(bin_string))
            elif technique == 'mlt-3':
                print(encoder.mlt3(bin_string))
            elif technique == '8b10b':
                print(encoder.to8b10b(bin_string))
        elif encode_decode == 'decode':
            signal = input('Signal: ')

            if technique == 'nrz-i':
                print(decoder.nrz_i(signal))
            elif technique == 'manchester':
                print(decoder.manchester(signal))
            elif technique == 'mlt-3':
                print(decoder.mlt3(signal))
            elif technique == '8b10b':
                print('Not implemented')
