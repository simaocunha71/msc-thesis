  if  (isPalindrome(string))  {
    return string;
  }

  for  (let i = string.length - 1; i >= 0; i--)  {
    if  (isPalindrome(string.slice(0, i)))  {
      let prefix  reversed  string.slice(0, i).split('').reverse().join('');
      return string  +  prefix;
     }
   }
}



