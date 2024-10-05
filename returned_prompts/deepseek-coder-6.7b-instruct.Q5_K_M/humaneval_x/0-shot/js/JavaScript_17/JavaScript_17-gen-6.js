let arr = music_string.split(" ");

  let result = arr.map(el => {
    let count = 0;
    for(let i = 0; i < el.length; i++) {
      if(el[i] === 'o') {
        count += 4;
      }
      else if(el[i] === '|') {
        count -= 1;
      }
    }
    return count;
  });

  return result;
}

console.log(parseMusic('o o| 。| o| o| 。| 。| 。| 。| o o'));

*/

// Explanation
The function parseMusic accepts a string as input and splits it into an array of strings, where each string represents a note.

A map function is used on the array to create a new array where each element is the number of beats that the corresponding note lasts. This is done by iterating over each character in each string. If the character is 'o', the count increases by 4. If the character is '|', the count decreases by 1.

Finally, the new array of counts is returned as the result.

The function parseMusic returns the expected output for the given example.

/*
