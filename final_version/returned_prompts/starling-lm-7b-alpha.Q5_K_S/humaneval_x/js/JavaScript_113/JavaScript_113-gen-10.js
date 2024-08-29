  return lst.map(s => {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
      if (Number(s[i]) % 2 != 0) {
        count += 1;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count}f the ${count}nput.`;
  });
}



