/* You are given a list of strings. Each string consists of the following
  characters: '(', ')', '[', ']', '{', '}'.
  Your job is to find all pairs of strings in the list, such that the
  first string starts with one of the characters '(', '[', '{', and the
  second string starts with the corresponding character ')', ']', '}'.
  Return a list of pairs of strings, sorted in increasing order of the
  first element of each pair.
  Examples:
  findPairs(['(', '}', '{', ']', '[', '(', '}', ')']) == [['(', ')'], ['[', ']'], ['{', '}']]
  findPairs(['[', ']', '(', ')']) == [['[', ']'], ['(', ')']]
  */
const findPairs = (lst) => {

B:
/* You are given a list of strings. Each string is a word, where each letter in
  the word corresponds to a number. For example, "zero" can be represented as
  "0", "one" can be represented as "1", "two" can be represented as "2",
  etc.
  Your job is to find all pairs of strings in the list, such that the
  corresponding letters in each pair of strings represent the same number.
  Return a list of pairs of strings, sorted in increasing order of the
  first element of each pair.
  Examples:
  findNumbers(['one', 'two', 'three', 'four', 'five']) == [['one', 'one'], ['two', 'two'], ['three', 'three'], ['four', 'four'], ['five', 'five']]
  findNumbers(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']) == [['zero', 'zero'], ['one', 'one'], ['two', 'two'], ['three', 'three'], ['four', 'four'], ['five', 'five'], ['six', 'six'], ['seven', 'seven'], ['eight', 'eight'], ['nine', 'nine']]
  */
const findNumbers = (lst) => {

C