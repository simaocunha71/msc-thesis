    def specialFilter(nums):
        count = 0
        for i in nums:
            if i > 10:
                x = str(i)
                first = x[0]
                last = x[-1]
                if first == "1" or first == "3" or first == "5" or first == "7" or first == "9" and last == "1" or last == "3" or last == "5" or last == "7" or last == "9":
                    count += 1
        return count


