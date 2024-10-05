  return lst.map(s => {
    let count = 0;
    for (let c of s) {
      if (parseInt(c) % 2 === 1) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
}



