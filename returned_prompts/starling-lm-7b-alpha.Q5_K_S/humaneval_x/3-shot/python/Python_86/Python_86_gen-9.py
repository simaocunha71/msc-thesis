    def anti_shuffle(s):
        result = ""
        for word in s.split():
            result += "".join(sorted(word)) + " "
        return result.strip()


