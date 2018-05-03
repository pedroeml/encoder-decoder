from collections import deque
import pandas as pd


class Signal:
    def __init__(self, starting_signal='-'):
        self.signal = starting_signal
        self.signal_history = deque()

    def flip(self):
        """
        Flip the signal value stored at signal attribute. If it was + then it becomes - and vice-versa.
        The change is stored at the signal_history attribute.

        """
        self.signal = '+' if self.signal == '-' else '-'
        self.keep()

    def keep(self):
        """
        Stores the current signal value stored at the signal attribute.

        """
        self.signal_history.append(self.signal)

    def __str__(self):
        """
        Returns a string containing all stored signals.

        :return:
        :rtype: str
        """
        return ''.join(list(self.signal_history))


class SignalThreeLevel:
    def __init__(self, starting_signal='0'):
        self.signal = starting_signal
        self.signal_history = deque()

    def update(self):
        """
        Flip the signal by the following rules:
        If current signal isn't 0, the next signal is 0
        If current signal is 0, the next signal is the opposite of the last non-zero signal stored

        """
        if self.signal != '0':  # If current signal isn't 0
            self.signal = '0'
        elif self.signal_history:   # If signal_history isn't empty
            last_non_zero_signal = None

            for signal in reversed(self.signal_history):     # Find the last non zero signal
                if signal != '0':
                    last_non_zero_signal = signal
                    break

            if last_non_zero_signal is not None:    # If there is a last non-zero signal
                self.signal = '+' if last_non_zero_signal == '-' else '-'
            else:   # If there isn't a last non zero signal
                self.signal = '+'
        else:   # If signal_history is empty
            self.signal = '+'

        self.keep()

    def keep(self):
        """
        Stores the current signal value stored at the signal attribute.

        """
        self.signal_history.append(self.signal)

    def __str__(self):
        """
        Returns a string containing all stored signals.

        :return:
        :rtype: str
        """
        return ''.join(list(self.signal_history))


def nrz_i(bin_string):
    """
    Applies the NRZ-I technique to a string of bits.

    :param bin_string:
    :type bin_string: str
    :return:
    :rtype: str
    """
    signal_manager = Signal()

    for bin_digit in bin_string:
        if bin_digit == '0':
            signal_manager.keep()
        else:
            signal_manager.flip()

    return str(signal_manager)


def manchester(bin_string):
    """
    Applies the Manchester technique to a string of bits.

    :param bin_string:
    :type bin_string: str
    :return:
    :rtype: str
    """
    signal_manager = Signal()

    for bin_digit in bin_string:
        if bin_digit == '0':    # Generate +-
            if signal_manager.signal == '+':    # It's positive
                signal_manager.keep()   # +
                signal_manager.flip()   # -
            else:   # It's negative
                signal_manager.flip()   # +
                signal_manager.flip()   # -
        else:   # Generate -+
            if signal_manager.signal == '+':    # It's positive
                signal_manager.flip()   # -
                signal_manager.flip()   # +
            else:   # It's negative
                signal_manager.keep()   # -
                signal_manager.flip()   # +

    return str(signal_manager)


def mlt3(bin_string):
    """
    Applies the MLT-3 technique to a string of bits.

    :param bin_string:
    :type bin_string: str
    :return:
    :rtype: str
    """
    signal_manager = SignalThreeLevel()

    for bin_digit in bin_string:
        if bin_digit == '0':
            signal_manager.keep()
        else:
            signal_manager.update()

    return str(signal_manager)


def to8b10b(bin_string):
    if len(bin_string) % 8 != 0:
        raise Exception('Binary string must be formed of 8 by 8 bits.')

    df = pd.read_csv('full_8b10b.csv', dtype=str)

    bits_8b_list = [bin_string[i:i+8] for i in range(0, len(bin_string), 8)]

    bits_10b_list = deque()

    rd = -1

    for byte in bits_8b_list:
        value = None
        if rd == -1:
            value = df[df['H_A'].str.match(byte)]['RD_M(a_j)'].values[0]
        elif rd == 1:
            value = df[df['H_A'].str.match(byte)]['RD_P(a_j)'].values[0]

        bits_10b_list.append(value)

        count_zeros = value.count('0')
        count_ones = value.count('1')

        disparity = count_ones - count_zeros

        if rd == -1:
            if disparity == 2:
                rd = 1
        elif rd == 1:
            if disparity == -2:
                rd = -1

    bits_10b_string = ''.join(list(bits_10b_list))

    print('8B10B: %s' % bits_10b_string)

    return nrz_i(bits_10b_string)
