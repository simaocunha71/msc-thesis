  return lst.map(el => el.split('').reduce((acc, digit) => acc + (digit % 2), 0).toString()).map(count => `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`);
}



