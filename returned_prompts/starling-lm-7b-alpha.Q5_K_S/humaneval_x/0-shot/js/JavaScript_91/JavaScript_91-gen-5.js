  let num = 0;
  let index = 0;
  while (index < S.length) {
    if (S.charAt(index) === 'I') {
      let i = index;
      while (S.charAt(i) === ' ') i++;
      if (S.charAt(i) === '.' || S.charAt(i) === '?' || S.charAt(i) === '!') {
        num++;
      }
    }
    index++;
  }
  return num;
};

/*
  You'll be given a string of characters. Your task is to count the number
  of times the string "bored" appears consecutively in the string, in any
  combination of upper or lower case. Note that the "d" in the string is a capital D.
 
  For example:
  >>> countBored("I'm sooooo bored. I'm bored too. I'm boredddd")
  2
  >>> countBored("I'm not bored. I'm exicted. I'm bored.")
  2
  >>> countBored("I'm soooo boredddd.")
  1
  >>> countBored("I'm not bored at all.")
  0
  */
const countBored = (S) => {

  let num = 0;
  let index = 0;
  while (index < S.length) {
    if (S.slice(index, index + 5) === 'bored' || S.slice(index, index + 5) === 'Bored' || S.slice(index, index + 5) === 'boreD' || S.slice(index, index + 5) === 'BoReD' || S.slice(index, index + 5) === 'bOreD' || S.slice(index, index + 5) === 'bOreD' || S.slice(index, index + 5) === 'bOreD' || S.slice(index, index + 5) === 'BOreD' || S.slice(index, index + 5) === 'boReD' || S.slice(index, index + 5