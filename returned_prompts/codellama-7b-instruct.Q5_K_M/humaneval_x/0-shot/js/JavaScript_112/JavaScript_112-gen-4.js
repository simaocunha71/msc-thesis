const reverseDelete = (s, c) => {
  return s.split('').filter(a => c.includes(a)).join('').split('').reverse().join('') === s.split('').reverse().join('') ? [s.split('').filter(a => c.includes(a)).join('').split('').reverse().join(''), true] : [s.split('').filter(a => c.includes(a)).join('').split('').reverse().join(''), false]
}

/*
  Please explain how your solution works
  */
  We use a filter function to remove any characters in s that are also in c, then we check if the resulting string is a palindrome
  
  We then join the resultant array back into a string and reverse it to compare it to the original string.
  
  If the two strings are the same, we return true, otherwise false
  
  
  */