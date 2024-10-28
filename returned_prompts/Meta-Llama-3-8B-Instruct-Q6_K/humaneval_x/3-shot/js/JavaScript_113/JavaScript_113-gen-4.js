  return lst.map((str, index) => {
    let count = 0;
    for (let char of str) {
      if (parseInt(char) % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${index}ng ${index} of the ${index}nput.`;
  });
}