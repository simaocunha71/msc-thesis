```javascript
const intToMiniRoman = (number) => {
    const romanNumerals = [
        { value: 1000, numeral: 'm' },
        { value: 900, numeral: 'cm' },
        { value: 500, numeral: 'd' },
        { value: 400, numeral: 'cd' },
        { value: 100, numeral: 'c' },
        { value: 90, numeral: 'xc' },
        { value: 50, numeral: 'l' },
        { value: 40, numeral: 'xl' },
        { value: 10, numeral: 'x' },
        { value: 9, numeral: 'ix' },
        { value: 5, numeral: 'v' },
        { value: 4, numeral: 'iv' },
        { value: 1, numeral: 'i' }
    ];

    let result = '';

    for (const numeral of romanNumerals) {
        while (number >= numeral.value) {
            result += numeral.numeral;
            number -= numeral.value;
        }
    }

    return result.toLowerCase();
};
```
Explanation:

1. Define an array of objects, each representing a roman numeral value and its corresponding numeral.
2. Initialize an empty string `result` to store the roman numeral equivalent.
3. Iterate through the `romanNumerals` array. For each iteration, check if the `number` is greater than or equal to the `value` of the current numeral.
4. If it is, add the corresponding numeral to the `result` string and subtract the `value` from the `number`. Repeat this process until the `number` is less than the `value`.
5. Finally, return the `result` string in lowercase.

Note: This implementation only handles numbers up to 1000, as per the problem restrictions. For larger numbers, additional roman numerals would need to be added to the array.