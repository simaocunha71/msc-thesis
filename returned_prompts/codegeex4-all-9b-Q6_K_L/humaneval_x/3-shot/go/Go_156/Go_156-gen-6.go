    // Roman numerals are created from the following symbols:
    // I = 1
    // V = 5
    // X = 10
    // L = 50
    // C = 100
    // D = 500
    // M = 1000

    // The value of a symbol is the value of the symbol itself
    // if it appears alone, but is 1 less if it appears before
    // a symbol with a higher value.

    // So MCDXCIV == 1000 + 500 + (100 - 10) + (10 - 1) + (5 - 1) + 4 = 1944
    // and CCXXV == 100 + 100 + 10 + 10 + 5 = 225

    // The exception to this rule is when a symbol appears 3 or more times
    // in a row, as in CCC or III. In this case the value of the symbol
    // is added to the total 3 times.

    // So IIII == 4, but IV == 4 as well
    // And MCM == 1900, and MCMX == 1900 as well

    // So, to convert an integer to a roman numeral, you need to find
    // the largest possible symbol that can be used to represent the number,
    // subtract that value from the number, and repeat until the number
    // is 0.

    // The symbols are listed in order of their value, from highest to lowest.
    // So, the first symbol to try is M, the second is D, etc.

    // So, to convert an integer to a roman numeral, you need to find
    // the largest possible symbol that can be used to represent the number,
    // subtract that value from the number, and repeat until the number
    // is 0.

    // The symbols are listed in order of their value, from highest to lowest.
    // So, the first symbol to try is M, the second is D, etc.

    // So, to convert an integer to a roman numeral, you need to find
    // the largest possible symbol that can be used to represent the number,
    // subtract that value from the number, and repeat until the number
    // is 0.

    // The symbols are listed in order of their value, from highest to lowest.
   