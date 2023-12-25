/*Task
  Write a function that takes a string as input and returns the sum of the upper characters only'
  ASCII codes.

  Examples:
      digitSum("") => 0
      digitSum("abAB") => 131
      digitSum("abcCd") => 67
      digitSum("helloE") => 69
      digitSum("woArBld") => 131
      digitSum("aAaaaXa") => 153
  */
const digitSum = (s) => {
  let sDigit = "";
  for(let i = 0, len = s.length; i < len; ++i){
    if((48 > i && i + 1 < len) || (97 > i && i + 1 < len)){
      sDigit += s[i];
    } else {
      return parseInt(sDigit);
    }
  }
};
digitSum("").
console.log("sum of uppercase only characters: ", digitSum('aAbCd'));
