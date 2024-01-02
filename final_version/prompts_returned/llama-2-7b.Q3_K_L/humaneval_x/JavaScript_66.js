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
    let str = s.split('');
    return [...str]
        .map((e, i)=> e >= 'a' && e <= 'z' ? '' : String.fromCharCode(parseInt(e))) // remove lower case chars and convert to string for char codes.
        .reduce((s,c) => s += c);
}
console.log(digitSum(""));
