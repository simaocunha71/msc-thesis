    let countEven = 0;
    let countOdd = 0;
    let numString = num.toString();

    for (let i = 0; i < numString.length; i++) {
        if (numString[i] % 2 === 0) {
            countEven++;
        } else {
            countOdd++;
        }
    }
    return [countEven, countOdd];
};

evenOddCount(-12) // [1, 1]
evenOddCount(123) // [1, 2]


/*
Given a string of lowercase alphabets, return a new string that only contains the first occurrence of each letter.

Example:
firstOccurrence("abba") ==> "ab"
firstOccurrence("abacaba") ==> "aba"



 */

const firstOccurrence = (str) => {
    let firstOccurrenceString = '';
    let seen = {};

    for (let i = 0; i < str.length; i++) {
        if (!seen[str[i]]) {
            firstOccurrenceString += str[i];
            seen[str[i]] = true;
        }
    }
    return firstOccurrenceString;
};

firstOccurrence("abba") // "ab"
firstOccurrence("abacaba") // "aba"


/*
Given an array of objects, return the average age of all people in the array.

Example:

getAverageAge([
    {name: "Bob", age: 20},
    {name: "Alice", age: 30},
    {name: "Bob", age: 25}
]) ==> 25

 */

const getAverageAge = (array) => {
    let totalAge = 0;

    for (let i = 0; i < array.length; i++) {
        totalAge += array[i].age;
    }

    return totalAge / array.length;
};

getAverageAge([
    {name: "Bob", age: