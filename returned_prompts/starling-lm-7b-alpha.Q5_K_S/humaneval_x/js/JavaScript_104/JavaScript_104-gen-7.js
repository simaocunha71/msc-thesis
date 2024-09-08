  let result = [];
  x.forEach(element => {
    if (
      (element < 10 && element % 2 === 1) ||
      (element < 100 && element % 2 === 1) ||
      (element < 1000 && element % 2 === 1) ||
      (element < 10000 && element % 2 === 1) ||
      (element < 100000 && element % 2 === 1)
    ) {
      result.push(element);
    }
  });

  return result.sort(function(a, b) { return a - b; });
}



