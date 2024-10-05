    def is_bored(S):
        i = 0
        while i < len(S):
            if S[i] == 'I':
                while S[i] != '.' and S[i] != '?' and S[i] != '!':
                    i += 1
                return True
            i += 1
        return False



