  let len = string.length;

  for  (let i = len; i >= 0; i--)  {
    if  (isPalindrome(string.substring(0, i)))  {
      return string + string.substring(0, len - i).split('').reverse().join('');
     }
   }

  return '';
}



