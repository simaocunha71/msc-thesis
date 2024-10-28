    def anti_shuffle(s):
        char_list = list(s)
        for i in range(len(char_list)):
            char_list[i] = "".join(sorted(char_list[i]))
        return "".join(char_list)


