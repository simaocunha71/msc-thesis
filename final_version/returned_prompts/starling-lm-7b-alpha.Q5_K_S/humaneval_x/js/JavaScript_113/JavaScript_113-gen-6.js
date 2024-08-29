  let result = [];
  for (let s of lst) {
    let count = 0;
    for (let c of s) {
      if (parseInt(c) % 2 == 1) {
        count += 1;
      }
    }
    result.push(`the number of odd elements ${count}n the str${count}ng ${count}f the ${count}nput.`);
  }
  return result;
}



