    def is_nested(string):
        cnt = 0
        for c in string:
            if c == '[':
                cnt += 1
            elif c == ']':
                cnt -= 1

            if cnt < 0:
                return True

        return cnt == 0


