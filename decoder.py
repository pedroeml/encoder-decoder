from collections import deque


class Binary:
    def __init__(self, starting_binary='0'):
        self.bit = starting_binary
        self.bit_history = deque()

    def flip(self):
        """
        Flip the bit value stored at bit attribute. If it was 1 then it becomes 0 and vice-versa.
        The change is stored at the bit_history attribute.

        """
        self.bit = '0' if self.bit == '1' else '1'
        self.keep()

    def keep(self):
        """
        Stores the current bit value stored at the bit attribute.

        """
        self.bit_history.append(self.bit)

    def __str__(self):
        """
        Returns a string containing all stored bits.

        :return:
        :rtype: str
        """
        return ''.join(list(self.bit_history))


def nrz_i(signal_string):
    """
    Decodes a string of signals encoded by NRZ-I technique.

    :param signal_string:
    :type signal_string: str
    :return:
    :rtype: str
    """
    bit_manager = Binary()

    previous_signal = None
    for signal in signal_string:
        if previous_signal is None:
            if signal == '-':
                bit_manager.keep()
            else:
                bit_manager.flip()
        else:
            if signal == previous_signal:
                if bit_manager.bit == '0':
                    bit_manager.keep()
                else:
                    bit_manager.flip()
            else:
                if bit_manager.bit == '1':
                    bit_manager.keep()
                else:
                    bit_manager.flip()

        previous_signal = signal

    return str(bit_manager)


def manchester(signal_string):
    """
    Decodes a string of signals encoded by Manchester technique.

    :param signal_string:
    :type signal_string: str
    :return:
    :rtype: str
    """
    if len(signal_string) % 2 != 0:
        raise Exception('The list must be even because it has to be decoded by pairs of signals.')

    bit_manager = Binary()

    previous_signal = None

    for signal in signal_string:
        if previous_signal is None:
            previous_signal = signal
        else:
            if signal == previous_signal:
                raise Exception('A pair of signals can\'t be of the same type.')
            else:
                if previous_signal == '+' and signal == '-':
                    if bit_manager.bit == '0':
                        bit_manager.keep()
                    else:
                        bit_manager.flip()
                else:
                    if bit_manager.bit == '0':
                        bit_manager.flip()
                    else:
                        bit_manager.keep()

            previous_signal = None

    return str(bit_manager)
