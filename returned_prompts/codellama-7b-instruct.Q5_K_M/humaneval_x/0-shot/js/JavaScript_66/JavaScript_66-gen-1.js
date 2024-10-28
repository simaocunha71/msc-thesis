const digitSum = (s) => {
  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (/[A-Z]/.test(s[i])) {
      sum += s[i].charCodeAt();
    }
  }
  return sum;
};

