const allPrefixes = (string) => {
    let array = [];
    for (let i = 1; i <= string.length; i++) {
        array.push(string.slice(0, i));
    }
    return array;
};

/* Return a list of all substrings of the input string, excluding the original string
  >>> substrings('abc')
  ['a', 'ab', 'abc', 'b', 'bc', 'c']
  */

const substrings = (string) => {
    let array = [];
    for (let i = 0; i < string.length; i++) {
        for (let j = i + 1; j <= string.length + 1; j++) {
            array.push(string.slice(i, j));
        }
    }
    return array;
};

/* Return a list of all permutations of the input string
  >>> permutations('abc')
  ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
  */

const permutations = (string) => {
    if (string.length === 1) {
        return [string];
    }
    let array = [];
    for (let i = 0; i < string.length; i++) {
        let char = string[i];
        let remainingString = string.slice(0, i) + string.slice(i + 1);
        let subPermutations = permutations(remainingString);
        subPermutations.forEach(perm => {
            array.push(char + perm);
        });
    }
    return array;
};

/* Return the number of times the input string can be divided evenly by the divisor
  >>> numberOfDivisions('abc', 'b')
  0
  >>> numberOfDivisions('aaabbbc', 'ab')
  2
  */

const numberOfDivisions = (string, divisor) => {
    let counter = 0;
    for (let i = 0; i < string.length; i++) {
        if (string.slice(i, i + divisor.length) === divisor