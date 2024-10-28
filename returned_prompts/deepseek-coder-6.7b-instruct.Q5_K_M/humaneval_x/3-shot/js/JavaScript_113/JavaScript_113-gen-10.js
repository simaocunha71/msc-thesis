  return lst.map(el => {
    let count = [...el].reduce((acc, cur) => acc + (cur % 2), 0);
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
}



