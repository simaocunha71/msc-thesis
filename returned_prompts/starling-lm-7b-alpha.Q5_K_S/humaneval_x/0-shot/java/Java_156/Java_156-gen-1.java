    String[] numerals = {
        "m", "cm", "d", "cd", "c", "xc", "l", "xl", "x",
        "ix", "v", "iv", "i"
    };
    int[] values = {
        1000, 900, 500, 400, 100, 90, 50, 40, 10,
        9, 5, 4, 1
    };

    StringBuilder roman = new StringBuilder();
    for (int i = 0; i < numerals.length; i++) {
        while (number >= values[i]) {
            roman.append(numerals[i]);
            number -= values[i];
        }
    }
    return roman.toString();
}
}



class Test(object):
    def __init__(self):
        self.solution = Solution()

    def run(self):
        print(self.solution.intToMiniRoman(19))
        print(self.solution.intToMiniRoman(152))
        print(self.solution.intToMiniRoman(426))

if __name__ == '__main__':
    Test().run()














































































































































































































