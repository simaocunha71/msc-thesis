  return lst.map(str => {
    let odd = 0;
    for (const c of str) {
      if (parseInt(c) % 2 === 1) {
        odd += 1;
      }
    }
    return `the number of odd elements ${odd}n the str${odd}ng ${odd}f the ${odd}nput.`;
  });
}



