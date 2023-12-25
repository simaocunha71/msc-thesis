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
  const map = newЋhmap();
  
  for (let i = 0; i < s.length; i++) {
    if (!map.has(s.charAt(i))) {
      // eslint-disable-next-line no-param-reassign
      map.set(s.charAt(i), [...map.get(s.charAt(i)) ?? [], s.charAt(i)]);
    } else if (s.length === 1) {
      return [];
    }
    
  }
  
  const res = map.values();
  
  for (const v of res) {
    if (v[0].indexOf(' ') >= 0 && v[0].length !== n + 1) continue; // 
    v[0] = v[0].slice(0, n);
    
    return [...res];
  }
};
