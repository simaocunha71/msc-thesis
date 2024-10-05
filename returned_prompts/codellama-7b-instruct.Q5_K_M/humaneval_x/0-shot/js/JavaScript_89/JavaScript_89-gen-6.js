
function encrypt(s){

  let newStr = '';
  for (let i = 0; i < s.length; i++) {
    if(s[i].charCodeAt(0) > 64 && s[i].charCodeAt(0) < 91){
      newStr += String.fromCharCode(s[i].charCodeAt(0) + 2 * 2);
    } else if (s[i].charCodeAt(0) > 96 && s[i].charCodeAt(0) < 123){
      newStr += String.fromCharCode(s[i].charCodeAt(0) + 2 * 2 - 32);
    } else {
      newStr += s[i];
    }
  }

  return newStr;

}
