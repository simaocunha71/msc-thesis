/*You are given an array of strings, where each string is a word.
  You have to return a new array, where the words are sorted by their length.
  If two or more words have the same length, sort them by their lexicographical order.

  [input/output] samples:
  sortByLength(["hello", "world", "javascript", "java", "c", "c++"]) ==
  ["c", "c++", "hello", "java", "javascript", "world"]
  sortByLength(["apple", "banana", "cherry", "kiwi", "mango", "orange"]) ==
  ["kiwi", "orange", "apple", "banana", "cherry", "mango"]
  sortByLength(["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"]
  sortByLength(["apple", "banana", "cherry", "kiwi", "mango", "orange", "a"]) ==
  ["a", "apple", "banana", "cherry", "kiwi", "mango", "orange"]
  */
const sortByLength = (arr) => {

B:
/*You are given a string, which represents a mathematical expression.
  You have to evaluate the expression and return the result.
  The expression may contain the following elements:
    - Integers, e.g. 1, 2, 3, ...
    - Operators, e.g. +, -, *, /
    - Brackets, e.g. (, ), {, }, [, ]
  The expression is always valid.
  You have to use a stack data structure to evaluate the expression.
  Note that there may be multiple solutions for a given expression.

  [input/output] samples:
  evaluate("(1 + 2) * 3") == 9
  evaluate("(1 + (2 * 3) + (4 * (5 + 6)))") == 57
  evaluate("2 * (2 + (3 * 4))") == 14
  evaluate("((1 + 2) * 3) + (4 * (5 + (