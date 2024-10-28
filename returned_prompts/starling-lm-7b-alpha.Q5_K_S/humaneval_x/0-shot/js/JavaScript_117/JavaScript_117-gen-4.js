const consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];

let result = [];
let word = "";
let count = 0;

for (let i = 0; i < s.length; i++) {
  const char = s[i];

  if (i === 0) {
    word += char;

    if (!consonants.includes(word[0].toLowerCase())) {
      word = "";
    }
  } else if (!consonants.includes(char.toLowerCase())) {
    if (count === n) {
      result.push(word);
      word = "";
      count = 0;
    } else {
      word += char;
      count++;
    }
  } else {
    word += char;
  }
}

return result;

};

selectWords("Mary had a little lamb", 4); // ["little"]
selectWords("Mary had a little lamb", 3); // ["Mary"]
selectWords("simple white space", 2); // []
selectWords("Hello world", 4); // ["world"]
selectWords("Uncle sam", 3); // ["Uncle"]


*/
selectWords("Mary had a little lamb", 4); // ["little"]
selectWords("Mary had a little lamb", 3); // ["Mary"]
selectWords("simple white space", 2); // []
selectWords("Hello world", 4); // ["world"]
selectWords("Uncle sam", 3); // ["Uncle"]





















































































