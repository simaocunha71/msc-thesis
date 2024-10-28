        String[] num = {"", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"};
        String[] tens = {"", "x", "xx", "xx", "xc", "l", "l", "l", "xc"};
        String[] hundreds = {"", "c", "cc", "cc", "cd", "d", "d", "d", "cd"};
        String[] thousands = {"", "m", "mm", "mm", "mcm", "m", "m", "m", "mcm"};

        String result = "";
        int count = 0;
        while (number > 0) {
            result = tens[number%10] + result;
            number /= 10;
        }
        return result;
    }
}



#python
def intToMiniRoman(number):
    num = "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"
    tens = "x", "xx", "xx", "xc", "l", "l", "l", "xc"
    hundreds = "c", "cc", "cc", "cd", "d", "d", "d", "cd"
    thousands = "m", "mm", "mm", "mcm", "m", "m", "m", "mcm"

    result = ""
    count = 0
    while number > 0:
        result = tens[number%10] + result
        number //= 10
    return result


#python
def intToMiniRoman(number):
    num = "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"
    tens = "x", "xx", "xx", "xc", "l", "l", "l", "xc"
    hundreds = "c", "cc", "cc", "cd", "d", "d", "d", "cd"
    thousands = "m", "mm", "mm", "mcm", "m", "m", "m", "