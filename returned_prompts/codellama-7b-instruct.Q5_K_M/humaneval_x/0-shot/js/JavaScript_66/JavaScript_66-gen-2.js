  const digitSum = (s) => {
    let sum = 0;
    for (let i = 0; i < s.length; i++) {
      const char = s[i];
      if (char === char.toUpperCase()) {
        sum += char.charCodeAt(0);
      }
    }
    return sum;
  };

