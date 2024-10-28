    let sum = 0;
    let product = 1;

    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
        product *= numbers[i];
    }

    return [sum, product];
};

sumProduct([1, 2, 3, 4]);

// Expected Output: [10, 24]






/*
  Count the total number of vowels in a given string. Vowels can be uppercase or lowercase.
  >>> countVowels('Hello, World!')
  3
  >>> countVowels('')
  0
  >>> countVowels('aBcDe')
  5
  >>> countVowels('aBcDeF')
  6
  >>> countVowels('12345')
  0
  >>> countVowels('!@#$%^&*()')
  0
  >>> countVowels('')
  0
*/

function countVowels(str) {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (vowels.includes(str[i].toLowerCase())) {
            count++;
        }
    }
    return count;
}

countVowels('Hello, World!');

// Expected Output: 3






/*
  Return the first word in a given sentence.
  >>> getFirstWord('Hello, World!')
  'Hello'
  >>> getFirstWord('')
  undefined
  >>> getFirstWord('The quick brown fox jumped over the lazy dog.')
  'The'
  >>> getFirstWord('The quick brown fox, jumped over the lazy dog.')
  'The'
  >>> getFirstWord('The quick brown fox jumped over the lazy dog, and barked at the moon.')
  'The'
  >>> getFirstWord('The quick brown fox jumped over the lazy dog, and barked at the moon')
 