  return lst.map(str => {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
      if ((str[i] - 0) % 2 == 1) {
        count += 1;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count}f the ${count}nput.`;
  });
}



