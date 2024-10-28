/* Filter an input list of strings only for ones that contain given substring
  >>> filterBySubstring([], 'a')
  []
  >>> filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')
  ['abc', 'bacd', 'array']
  */
  return strings.filter(string => string.includes(substring));
}

