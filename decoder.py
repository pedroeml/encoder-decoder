from collections import deque


class Binary:
    def __init__(self, starting_binary='0'):
        self.bit = starting_binary
        self.bit_history = deque()

    def flip(self):
        self.bit = '0' if self.bit == '1' else '1'
        self.keep()

    def keep(self):
        self.bit_history.append(self.bit)

    def __str__(self):
        return ''.join(list(self.bit_history))


def nrz_i(signal_string):
    binary_manager = Binary()

    previous_siginal = None
    for signal in signal_string:
        if previous_siginal is None:
            if signal == '-':
                binary_manager.keep()
            else:
                binary_manager.flip()
        else:
            # TODO: Fix this
            if signal == previous_siginal:
                if binary_manager.bit == '0':
                    binary_manager.keep()
                else:
                    binary_manager.flip()
            else:
                if binary_manager.bit == '1':
                    binary_manager.keep()
                else:
                    binary_manager.flip()

        previous_siginal = signal

    return str(binary_manager)
