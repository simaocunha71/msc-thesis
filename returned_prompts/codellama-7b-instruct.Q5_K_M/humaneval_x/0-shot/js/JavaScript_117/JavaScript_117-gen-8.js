/*Given a string s and a natural number n, you have been tasked to implement 
  a function that returns a list of all words from string s that contain exactly 
  n consonants, in order these words appear in the string s.
  If the string s is empty then the function should return an empty list.
  Note: you may assume the input string contains only letters and spaces.
  Examples:
  selectWords("Mary had a little lamb", 4) ==> ["little"]
  selectWords("Mary had a little lamb", 3) ==> ["Mary")
  selectWords("simple white space", 2) ==> []
  selectWords("Hello world", 4) ==> ["world"]
  selectWords("Uncle sam", 3) ==> ["Uncle"]
  */
const selectWords = (s, n) => {
    //split the string into an array of words
    const words = s.split(' ');
    const result = [];
    //iterate over the array of words
    words.forEach(word => {
        //count the consonants
        let count = 0;
        for (const char of word) {
            if (char !== 'a' && char !== 'e' && char !== 'i' && char !== 'o' && char !== 'u') {
                count++;
            }
        }
        //if the count is equal to the input, add the word to the result
        if (count === n) {
            result.push(word);
        }
    });
    //return the result
    return result;
}
