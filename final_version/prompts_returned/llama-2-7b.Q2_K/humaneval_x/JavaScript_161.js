/*You are given a string s.
  if s[i] is a letter, reverse its case from lower to upper or vise versa, 
  otherwise keep it as it is.
  If the string contains no letters, reverse the string.
  The function should return the resulted string.
  Examples
  solve("1234") = "4321"
  solve("ab") = "AB"
  solve("#a@C") = "#A@c"
  */
const solve = (s) => {
  let rstr = '';
  for(let i=0;i< s.length;i++){
    if(Character.isLetter(s[i])){//check letter type
      switch(s[i].toLowerCase()){ //check string type
        case "a":rstr += s[i] +'';break;
        default: rstr += Character(s[i]).toUpperCase(); break;
      }
    }else{//do nothing else with the character
      rstr+=Character(s[i]);break;}
  }return rstr;
}
module.exports = solve