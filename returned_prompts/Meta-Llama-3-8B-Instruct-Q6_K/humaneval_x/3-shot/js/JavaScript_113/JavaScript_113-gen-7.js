  return lst.map((str, idx) => {
    let count = 0;
    for (let char of str) {
      if (+char % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${str}ng ${idx+1} of the ${idx+1}nput.`;
  });
}