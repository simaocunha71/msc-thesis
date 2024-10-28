  return lst.map(str => {
    const oddCount = str.split('').filter(c => c % 2 != 0).length;
    return `the number of odd elements ${oddCount}n the str${oddCount}ng ${oddCount} of the ${oddCount}nput.`;
  });
}