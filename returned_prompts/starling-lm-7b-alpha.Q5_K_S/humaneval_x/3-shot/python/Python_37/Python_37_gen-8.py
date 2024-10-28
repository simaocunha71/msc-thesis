    def sort_even(l: list):
        sorted_even = []
        for i in range(0, len(l), 2):
            sorted_even.append(l[i])
            sorted_even.append(min(l[i+1:i+2]))
        return sorted_even


