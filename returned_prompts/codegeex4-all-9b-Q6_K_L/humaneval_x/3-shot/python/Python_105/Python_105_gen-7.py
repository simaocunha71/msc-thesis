    def get_name(number):
        return {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }.get(number, "")

    return [get_name(x) for x in sorted(arr) if 1 <= x <= 9][::-1]