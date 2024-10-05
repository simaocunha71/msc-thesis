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

  let sum = 0;
  const upper = s.toUpperCase();
  for (let i = 0; i < upper.length; i++) {
    sum += upper.charCodeAt(i);
  }
  return sum;
};
