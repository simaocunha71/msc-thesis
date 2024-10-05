
function isConsonant(char){
  return !['a', 'e', 'i', 'o', 'u'].includes(char)
}

let words = s.split(' ')
let res = []

for(let word of words){
  let count = 0
  for(let char of word){
    if(isConsonant(char)){
      count++
    }
  }
  if(count == n) {
    res.push(word)
  }
}

return res
};

selectWords("Mary had a little lamb", 4) // ["little"]
selectWords("Mary had a little lamb", 3) // ["Mary"]
selectWords("simple white space", 2) // []
selectWords("Hello world", 4) // ["world"]
selectWords("Uncle sam", 3) // ["Uncle"]


/*

Also you can use regex to solve this problem, here is the solution:

function selectWords(s, n) {
  const regex = new RegExp(`[^aeiou]{${n}}`, 'g');
  return s.match(regex)?.map(word => word.trim());
}

*/


*/
























































































































































































































