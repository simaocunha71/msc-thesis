    def by_length(arr):
        def name_num(num):
            return {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine"
            }.get(num, "None")

        arr = [name_num(num) for num in arr if 1 <= num <= 9]
        arr.sort(reverse=True)
        return arr




# Tests
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([1, -1, 55]))  # ["One"]
print(by_length([]))  # []
print(by_length([-1, 1, 5, 6, 7, 8, 9, 10]))  # ["Nine", "Eight", "Seven", "Six", "Five", "None", "None", "None"]
print(by_length([9, 9, 9, 9, 9, 9, 9, 9]))  # ["Nine", "Nine", "Nine", "Nine", "Nine", "Nine", "Nine", "Nine"]
print(by_length([1, 2, 3]))  # ["Three", "Two", "One"]
print(by_length([1, 2, 3, 4]))  # ["Four", "Three", "Two", "One"]
print(by_length([-1, 2, 3]))  # ["Two", "One"]
print(by_length([-1, -2, -3]))  # ["One"]
print(by_length([10, 11, 12, 13]))  # ["None", "None", "None", "None"]
print(by_length([