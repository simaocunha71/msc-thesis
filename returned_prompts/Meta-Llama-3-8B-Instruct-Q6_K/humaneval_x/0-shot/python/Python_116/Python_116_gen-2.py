    def sort_array(arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))  # Sort by number of ones in binary representation and then by decimal value.