  return lst.map(s => {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
      if (parseInt(s[i]) % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
}



