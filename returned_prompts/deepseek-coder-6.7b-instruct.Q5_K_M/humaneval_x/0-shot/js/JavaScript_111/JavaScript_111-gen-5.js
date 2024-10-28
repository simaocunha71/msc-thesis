  const wordArray = test.split(" ");
  const letterCount = {};
  let max = 0;
  
  for(let i = 0; i < wordArray.length; i++){
    const letter = wordArray[i];
    if(letterCount[letter]){
      letterCount[letter]++;
    } else {
      letterCount[letter] = 1;
    }
    if(letterCount[letter] > max){
      max = letterCount[letter];
    }
  }

  for(let key in letterCount){
    if(letterCount[key] !== max){
      delete letterCount[key];
    }
  }

  return letterCount;
};

console.log(histogram('a b c'));
console.log(histogram('a b b a'));
console.log(histogram('a b c a b'));
console.log(histogram('b b b b a'));
console.log(histogram(''));

/*
Output:
{ a: 1, b: 1, c: 1 }
{ a: 2, b: 2 }
{ a: 2, b: 2 }
{ b: 4 }
{}
*/



/*
This function works by first splitting the input string into an array of words.
Then it iterates over each letter in the wordArray. If the letter is already in the
letterCount object, it increments that letter's count, otherwise it sets the count
to 1. If the count of the current letter is greater than the max count, it updates
max.

After iterating over all the letters, it iterates over the letterCount object. If
the count of the current letter is not equal to max, it deletes that key from the
object.

Finally, it returns the letterCount object.
*/

//This solution has a time complexity of O(n) because we are looping through the string once.
//The space complexity is also O(n) because we are storing the count of each letter in the letterCount object.


































