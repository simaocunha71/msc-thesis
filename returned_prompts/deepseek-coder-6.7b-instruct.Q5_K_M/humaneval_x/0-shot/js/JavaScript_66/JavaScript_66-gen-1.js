let sum = 0;

for (let i = 0; i < s.length; i++) {
  let charCode = s.charCodeAt(i);
  if (charCode >=65 && charCode <=90) {
    sum += charCode;
  }
}

return sum;
}
console.log(digitSum("abAB"));
console.log(digitSum("abcCd"));
console.log(digitSum("helloE"));
console.log(digitSum("woArBld"));
console.log(digitSum("aAaaaXa"));

