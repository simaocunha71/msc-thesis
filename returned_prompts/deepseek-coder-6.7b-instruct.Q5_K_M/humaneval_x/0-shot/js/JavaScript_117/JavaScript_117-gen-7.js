  if(s === '') return [];
  
  const words = s.split(' ');
  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
  
  return words.filter(word => {
    let count = 0;
    for(let i = 0; i < word.length; i++){
      if(consonants.includes(word[i])) count++;
    }
    return count === n;
  });
};

console.log(selectWords("Mary had a little lamb", 4)); // ["little"]
console.log(selectWords("Mary had a little lamb", 3)); // ["Mary"]
console.log(selectWords("simple white space", 2)); // []
console.log(selectWords("Hello world", 4)); // ["world"]
console.log(selectWords("Uncle sam", 3)); // ["Uncle"]



/*
  The function selectWords takes two parameters, a string s and a number n. 
  The string s is split into words using the split(' ') method and stored in the variable words.
  Then, for each word in the words array, a for loop is used to count the number of consonants in the word.
  If the count of consonants is equal to n, the word is added to the result array.
  Finally, the result array is returned.
  */

/*
  The time complexity of this function is O(n*m) where n is the number of words in the string and m is the average length of the words.
  The space complexity is O(n) where n is the number of words in the string.
  */

/*
  This function is case-sensitive, meaning it treats 'a' and 'A' as different characters.
  It also assumes that words are separated by spaces and that the input string does not contain any punctuation.
  */

/*
  This function can be useful in many applications such as text analysis, language processing, and so on.
  For example, it can be used in a simple spell checker to find words with a specified number of consonants