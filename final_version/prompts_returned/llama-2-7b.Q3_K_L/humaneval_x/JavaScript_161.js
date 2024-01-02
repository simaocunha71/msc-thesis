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
  let reversedString = '';
  for(let i=0;i< s.length;i++){
    if( /[a-z]/.test(s[i]) ){
      let index = s[i].toLowerCase().charCodeAt();
      if (index > 64 && index < 91){
        //let lowerIndex = [...s, ...s.slice(0, i)]
         reversedString+= s[i]
      }else{
        let letterIndex = [...s, ...s.slice(0, i)];
        if (index > 64 && index < 91){
          //let lowerIndex = [...s, ...s.slice(0, i)]
           reversedString+= s[i].toUpperCase()
         }else{
          let upperIndex = [...s, ...s.slice(0, i)];
          reversedString+=s[i]
        }
      }
    }
  }
  return reversedString
}