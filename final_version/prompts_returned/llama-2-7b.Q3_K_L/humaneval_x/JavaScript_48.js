/*
  Checks if given string is a palindrome
  >>> isPalindrome('')
  true
  >>> isPalindrome('aba')
  true
  >>> isPalindrome('aaaaa')
  true
  >>> isPalindrome('zbcd')
  false
  */
const isPalindrome = (text) => {
  if(text.length === 0 || text == "") return text;
  let result = "";
  for(let i = 0; i < text.length - 1; i++) {
    if((text[i] + text[text.length - 1]) != text[text.length - 1] + text[i]){
      return false
    } else {
      result += text[i];
    }
  }
  
  //console.log(result)
  return true;
};