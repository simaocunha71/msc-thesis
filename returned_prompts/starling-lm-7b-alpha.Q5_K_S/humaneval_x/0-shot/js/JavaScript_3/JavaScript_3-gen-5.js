    let balance = 0;
    let flag = false;
    for (let i = 0; i < operations.length; i++) {
        balance += operations[i];
        if (balance < 0) {
            flag = true;
            break;
        }
    }
    return flag;
};


/* You're given a string and a dictionary of words and their anagrams. Your task is to
  determine if the string is an anagram of any of the words in the dictionary. If so, return
  the first such word in the dictionary. Otherwise, return an empty string.
  >>> anagrams('listen', {'enlist': ['enlist'], 'google': ['glance']})
  'enlist'
  >>> anagrams('tacocat', {'tacocat': ['tacocat']})
  'tacocat'
  >>> anagrams('canoeing', {'ecnionay': ['ecnionay']})
  ''
  */
const anagrams = (str, dictionary) => {
    let chars = Array.from(str);
    chars.sort();
    let result = '';
    for (let key in dictionary) {
        let chars2 = Array.from(key);
        chars2.sort();
        if (chars.join('') === chars2.join('')) {
            result = key;
            break;
        }
    }
    return result;
};


/* You're given a string of lowercase alphabetical characters. Your task is to return a new
  string that contains every letter that appears more than once in the original string.
  >>> onlyOnce('hello')
  'lo'
  >>> onlyOnce('banana')
  'aaan'
  >>> onlyOnce('abcabc')
  'c'
  */
const onlyOnce = (str) => {
    let result = '';
    for (let i = 0; i < str.length; i++) {
        if (str.indexOf(str[i]) !== str.lastIndexOf(str[i])) {
            result += str[i];
        }
    }
    return result;
};

