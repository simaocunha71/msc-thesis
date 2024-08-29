  return lst.map(str => {
    let count = 0;
    for (const c of str) {
      if (parseInt(c) % 2 != 0) {
        count += 1;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count}f the ${count}nput.`;
  });
}



