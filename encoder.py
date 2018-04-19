from collections import deque


class Signal:
    def __init__(self, starting_signal='-'):
        self.signal = starting_signal
        self.signal_history = deque()

    def flip(self):
        self.signal = '+' if self.signal == '-' else '-'
        self.keep()

    def keep(self):
        self.signal_history.append(self.signal)

    def __str__(self):
        return ''.join(list(self.signal_history))


def nrz_i(bin_string):
    signal_manager = Signal()

    for bin_digit in bin_string:
        if bin_digit == '0':
            signal_manager.keep()
        else:
            signal_manager.flip()

    return str(signal_manager)


def manchester(bin_string):
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
