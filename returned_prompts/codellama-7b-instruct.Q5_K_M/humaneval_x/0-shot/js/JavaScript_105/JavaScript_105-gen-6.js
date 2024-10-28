/*
  Given a string and an array of strings, return a new array where each string is
  repeated as many times as its length. For example, if the input string is "abc" and the input array is ["abc", "def", "ghi"], then the output array should be ["abc", "abc", "abc", "def", "def", "def", "ghi", "ghi", "ghi"].

  If the input array is [], then you should simply return [].
  If the input string is "", then you should return [].
  
  for example:
  ['abc', 'def', 'ghi'] -> ['abc', 'abc', 'abc', 'def', 'def', 'def', 'ghi', 'ghi', 'ghi']
  ['abc', 'def'] -> ['abc', 'abc', 'def', 'def']
  [] -> []
  */
const repeat = (str, arr) => {

