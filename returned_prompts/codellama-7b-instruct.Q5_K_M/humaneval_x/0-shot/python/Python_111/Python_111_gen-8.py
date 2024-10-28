
    def histogram(test):
        test = test.split()
        count = {}
        for i in test:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return count