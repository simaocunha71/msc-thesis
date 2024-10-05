    let i = 0
    while (string[i]) {
        i++
    }
    return i
};
/* Return the first index of the given string in the big string
  >>> find('', '')
  -1
  >>> find('abc', 'abc')
  0
  >>> find('abc', 'ac')
  0
  >>> find('abc', 'abcdef')
  0
  >>> find('abc', 'abcxyz')
  3
  */
const find = (big, small) => {
    for (let i = 0, l = big.length; i < l; i++) {
        if (big[i] === small[0]) {
            if (big.slice(i, i + small.length) === small) {
                return i
            }
        }
    }
    return -1
};
/* Capitalize the given string
  >>> cap('')
  ''
  >>> cap('abc')
  'abc'
  >>> cap('abcdef')
  'ABCDEF'
  */
const cap = (string) => {
    let result = ''
    for (const char of string) {
        if (char === char.toUpperCase()) {
            result += char
        } else {
            result += char.toUpperCase()
        }
    }
    return result
};
/* Reverse the given string
  >>> rev('')
  ''
  >>> rev('abc')
  'cba'
  >>> rev('abcdef')
  'fedcba'
  */
const rev = (string) => {
    let result = ''
    for (const char of string) {
        result = char + result
    }
    return result
};
/* Remove all vowels from the given string
  >>> removeVowels('')
  ''
  >>> removeVowels('abc')
  'bc'
  >>> removeVowels('abcdef')
  'bcdf'
  */
const removeVowels = (string) => {
    const vowels = ['a', 'e', 'i', 'o', 'u']
    for (const vowel of vowels) {
