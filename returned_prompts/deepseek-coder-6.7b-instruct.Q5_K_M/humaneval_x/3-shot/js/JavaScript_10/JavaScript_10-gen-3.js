  if  (isPalindrome(string))  {
    return string;
  }

  for  (let i = string.length - 1; i >= 0; i--)  {
    if  (isPalindrome(string.slice(0, i)))  {
      let prefix  reverse  string.slice(0, i);
      return string  +  prefix;
     }
   }
}



