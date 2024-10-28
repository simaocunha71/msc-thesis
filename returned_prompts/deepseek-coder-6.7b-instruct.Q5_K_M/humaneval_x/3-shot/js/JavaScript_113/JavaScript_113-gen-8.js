  return lst.map(str => {
    let count = 0;
    for(let char of str) {
      if(char % 2 !== 0) count++;
    }
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
}



