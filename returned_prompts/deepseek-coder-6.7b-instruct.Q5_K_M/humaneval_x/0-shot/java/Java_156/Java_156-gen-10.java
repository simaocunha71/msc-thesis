        StringBuilder roman = new StringBuilder();

        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};

        for (int i = 0; i < values.length && number >= 0; i++) {
            while (values[i] <= number) {
                roman.append(symbols[i]);
                number -= values[i];
            }
        }

        return roman.toString();
    }
}


A: This is a simple problem of converting a decimal number to a roman number. You can solve this by creating an array for the values and symbols of the roman numerals. Then you can loop over the array and append the corresponding roman numeral to the result string as long as the number is greater than or equal to the current value.

Here is the code in Java:

```java
public String intToRoman(int num) {
    int[] values = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    String[] symbols = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

    StringBuilder roman = new StringBuilder();

    for(int i=0; i<values.length && num>=0; i++){
        while(values[i]<=num){
            roman.append(symbols[i]);
            num -= values[i];
        }
    }

    return roman.toString();
}
```

This code starts from the highest value in the values array and keeps subtracting it from the input number until it can no longer be subtracted. It then moves on to the next value in the array and continues this process until it has gone through all the values.