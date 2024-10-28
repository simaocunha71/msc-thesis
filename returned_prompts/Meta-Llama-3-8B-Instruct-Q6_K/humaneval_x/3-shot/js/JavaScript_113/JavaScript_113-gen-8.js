  return lst.map((str, i) => {
    let count = 0;
    for (const c of str) {
      if (parseInt(c) % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${i}ng ${i} of the ${i}nput.`;
  });
}