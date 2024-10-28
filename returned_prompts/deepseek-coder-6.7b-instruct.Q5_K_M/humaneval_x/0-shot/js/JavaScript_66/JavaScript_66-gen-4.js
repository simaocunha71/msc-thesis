  let sum = 0;

  for(let i = 0; i < s.length; i++) {
    let char = s.charCodeAt(i);

    if(char >= 65 && char <= 90) {
      sum += char;
    }
  }

  return sum;
};

console.log(digitSum("abAB"));  // 131
console.log(digitSum("abcCd"));  // 67
console.log(digitSum("helloE"));  // 69
console.log(digitSum("woArBld"));  // 131
console.log(digitSum("aAaaaXa"));  // 153

