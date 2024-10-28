  const countChars = (str) => str.split('').reduce((acc, char) => {
    acc[char] = (acc[char] || 0) + 1;
    return acc;
  }, {});

  const count0 = countChars(s0);
  const count1 = countChars(s1);

  if (Object.keys(count0).length !== Object.keys(count1).length) {
    return false;
  }

  for (let char in count0) {
    if (count0[char] !== count1[char]) {
      return false;
    }
  }

  return true;
}
*/

// 2nd Solution:
/*
