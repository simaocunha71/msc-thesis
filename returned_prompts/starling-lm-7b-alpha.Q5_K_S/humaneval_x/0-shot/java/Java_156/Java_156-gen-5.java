        if(number < 0) {
            return "-" + intToMiniRoman(-number);
        }
        char[][] roman = {
            {1000,"M"},
            {900,"CM"},
            {500,"D"},
            {400,"CD"},
            {100,"C"},
            {90,"XC"},
            {50,"L"},
            {40,"XL"},
            {10,"X"},
            {9,"IX"},
            {5,"V"},
            {4,"IV"},
            {1,"I"}
        };
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < roman.length; i++) {
            while (number >= roman[i][0]) {
                sb.append(roman[i][1]);
                number -= roman[i][0];
            }
        }
        return sb.toString();
    }
}


# Python 3
def intToMiniRoman(number):
    """ Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> intToMiniRoman(19) == "xix"
    >>> intToMiniRoman(152) == "clii"
    >>> intToMiniRoman(426) == "cdxxvi"
    """
    if number < 0:
        return "-" + intToMiniRoman(-number)
    roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    result = ""
    for i in range(len(values)):
        while number >= values[i]:
            result += roman[i]
            number -= values[i]
    return result

# Python 3
def intTo