  const helper = (arr, idx) => {
    const ones = arr
      .map(x => x.toString(2))
      .map(x => x.split('1').length - 1)
      .reduce((a, b) => a + b);

    return arr.sort((a, b) => {
      const aOnes = helper(arr.slice(idx, idx + a.length).map(x => parseInt(x)), 0).reduce((a, b) => a + b);
      const bOnes = helper(arr.slice(idx, idx + b.length).map(x => parseInt(x)), 0).reduce((a, b) => a + b);
      return aOnes === bOnes ? a - b : aOnes - bOnes;
    });
  };

  return helper(arr, 0);
};



