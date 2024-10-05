    def digit_to_name(num):
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
        }[num]

    return [digit_to_name(num) for num in sorted([num for num in arr if 1 <= num <= 9], reverse=True)]