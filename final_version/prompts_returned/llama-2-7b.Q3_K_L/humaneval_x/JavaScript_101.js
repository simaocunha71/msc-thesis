/*
  You will be given a string of words separated by commas or spaces. Your task is
  to split the string into words and return an array of the words.
  
  For example:
  wordsString("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
  wordsString("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
  */
const wordsString = (s) => {
  const res = [];
  let i = 0;

  while ((i < s.length)) {
    if (s[i].match(/[\w+]/gi)) {
      i++;
    } else {
      res.push(s[i]);
      i++;
    }
  }

  return res;
};