longest(['a', 'bb', 'ccc'])
longest(['a', 'bb', 'ccc'])
longest([])


longest = (strings) => {
  if(strings.length === 0) {
    return null;
  }

  let max = strings[0];
  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > max.length) {
      max = strings[i];
    }
  }
  return max;
};







/* Find the longest of all the strings in the given list. If there are multiple longest strings,
  return the first one that you encounter. Return null if the list is empty.
  >>> longest([])
  >>> longest(['a', 'b', 'c'])
  'a'
  >>> longest(['a', 'bb', 'ccc'])
  'ccc'

  >>> longest(['aa', 'bb', 'cccccc', 'aa', 'bb'])
  'aaaaaa'
  >>> longest(['aa', 'bb', 'cccccc', 'aa', 'bb', 'bb'])
  'cccccc'
  >>> longest(['aa', 'bb', 'cccccc', 'aa', 'bb', 'bb', 'cccccc'])
  'cccccc'
*/



/* Given an array of strings, return a new array with each string reversed. For example:
  >>> reverseStrings(['a', 'bb', 'ccc'])
  ['a', 'bb', 'ccc']
  >>> reverseStrings(['a', 'bb', 'cccccc'])
  ['a', 'bb', 'cccccc']
  >>> reverseStrings(['aa', 'bb', 'cccccc', 'aa', 'bb'])
  ['aa', 'bb', 'cccccc', 'aa', 'bb']
  >>> reverseStrings([])
  []
*/



/* Given an array of strings, return a new array with each string reversed. For example:
  >>> reverseStrings(['a', 'bb', 'ccc'])
  ['a', 'bb', 'ccc']
  >>> reverseStrings(['a', 'bb', 'cccccc'])
  ['a', 'bb', 'cccc