  return lst.map(s => {
    var count = 0;
    for (const c of s) {
      if (parseInt(c) % 2 == 1) {
        count += 1;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count}f the ${count}nput.`;
  });
}



