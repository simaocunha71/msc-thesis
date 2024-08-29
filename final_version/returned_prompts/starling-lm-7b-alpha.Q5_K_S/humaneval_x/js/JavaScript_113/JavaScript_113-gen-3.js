  return lst.map(str => {
    let count = 0;
    for (const d of str) {
      if (Number(d) % 2 != 0) {
        count += 1;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count}f the ${count}nput.`;
  });
}



