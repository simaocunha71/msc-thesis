/* Create a function that takes 2 arguments, a string and a separator.
  Returns the string with the separator between each letter.
  Examples
  separate("hello", "|") ➞ "h|e|l|l|o"
  separate("hello", "-") ➞ "h-e-l-l-o"
  separate("hello", "") ➞ "hello"
  separate("hello", " ") ➞ "h e l l o"
  */
const separate = (string, seperator) => string.split("").join(seperator);

