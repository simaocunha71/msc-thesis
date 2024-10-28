    def anti_shuffle(s):
        arr = s.split(' ')
        for idx, word in enumerate(arr):
            arr[idx] = ''.join(sorted(word))

        return ' '.join(arr)


