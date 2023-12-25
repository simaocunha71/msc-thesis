/*
  Create a function that takes a string as input which contains only square brackets.
  The function should return true if and only if there is a valid subsequence of brackets
  where at least one bracket in the subsequence is nested.
  isNested('[[]]') ➞ true
  isNested('[]]]]]]][[[[[]') ➞ false
  isNested('[][]') ➞ false
  isNested('[]') ➞ false
  isNested('[[][]]') ➞ true
  isNested('[[]][[') ➞ true
  */
const isNested = (string) => {
  const substrings = string.split("]");
  const nestedLength = substrings.length;
  const nestedSubsequences = getValidSubsequences(nestedLength);
  return nestedSubsequences.some(([subsequence, isNestedSubsequence]) =>
    // Return true if at least one brackets is nested within the input string
    isNestedSubsequence && subsequence.length > 1;
  );
};
function getValidSubsequences(subsequencesLength) {
  const subsequences = Array(subsequencesLength + 1).fill("").map((_0, index) => (
    index < subsequencesLength ? [new Array(index + 1).fill(""), index] : []
  ));
  return subsequences;
}
