  for  (let i = string.length; i >= 0; i--)  {
    if  (isPalindrome(string.slice(0, i)))  {
      return string + string.slice(i).split('').reverse().join('');
     }
  }
}



