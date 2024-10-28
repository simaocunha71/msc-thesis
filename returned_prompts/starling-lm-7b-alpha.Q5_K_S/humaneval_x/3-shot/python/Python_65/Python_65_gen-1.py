    def circular_shift_helper(x, shift):
        if shift > len(x):
            return "".join(reversed(x))
        else:
            return "".join(
                [x[i % len(x)] for i in range(shift, len(x))] +
                [x[i] for i in range(shift)]
            )

    return circular_shift_helper(str(x), shift)


