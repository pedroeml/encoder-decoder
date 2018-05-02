from collections import deque


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
