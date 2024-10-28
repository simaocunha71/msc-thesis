  return lst.map((str, i) => {
    let count = 0;
    for (let char of str) {
      if (+char % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${i}ng ${i} of the ${i}nput.`;
  });
}