    def anti_shuffle(s: str) -> str:
        """
        >>> anti_shuffle('Hi')
        'Hi'
        >>> anti_shuffle('hello')
        'ehllo'
        >>> anti_shuffle('Hello World!!!')
        'Hello !!!Wdlor'
        """
        return ' '.join(''.join(sorted(word)) for word in s.split())



