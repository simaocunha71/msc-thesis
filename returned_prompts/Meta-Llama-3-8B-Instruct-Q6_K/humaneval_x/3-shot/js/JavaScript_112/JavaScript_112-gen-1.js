  let result = s.split('').filter(x => !c.includes(x)).join('');
  return [result, result === result.split('').reverse().join('')];
}  // This will return an array with the first element being the result string and the second element being the boolean value indicating whether the string is palindrome or not.