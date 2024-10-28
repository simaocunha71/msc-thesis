    def anti_shuffle(s):
        words = s.split()
        return ' '.join(''.join(sorted(word)) for word in words)

    print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'  # Test case


