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
