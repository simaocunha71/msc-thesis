/* Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
  should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
  alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
  Examples
  splitWords("Hello world!") ➞ ["Hello", "world!"]
  splitWords("Hello,world!") ➞ ["Hello", "world!"]
  splitWords("abcdef") == 3
  */
const splitWords = (txt) => {
  const regex = /[^\s]+/g; // regex matching non-whitespace characters
  const words = [];
  
  // If there are spaces, we need to split the string
  if(txt.includes(' ')) {
    let i, w;
    
    while ((i = txt.indexOf(regex))) {
      w = txt.substring(0, i);
      words.push(w)
      
      // If we find a comma, we stop at that point and return the list of words 
      if (txt[i] === ',') {
        break;
      }
    }
    
    words.push(txt.substring(txt.length - 1));
  
    // Return the list of words separated by commas
    return words.toString().replace(/,/g, ", ");
  } else {
    let r = [];
    for (let j = 'a'; j <= 'z'; ++j) {
      r += `${j},`;
      if (Character.isLetter(String.fromCharCode(parseInt(`&ord(${r.charAt(0).toLowerCase()})`)))) {
        return 26;
      } else {
        break; // Stop early at the first odd order letter, we are done if it is found.  
      }
    };
    
    return r.length -1 ;
  }
};
