  return lst.map((str) => {
    let count = 0;
    for (const c of str) {
      if (Number(c) % 2 == 1) {
        count += 1;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
}



