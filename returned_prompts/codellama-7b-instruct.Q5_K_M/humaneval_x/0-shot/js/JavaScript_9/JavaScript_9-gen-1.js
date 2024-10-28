  const result = [];
  let max = null;

  numbers.forEach(number => {

B:
    if (max === null || number >= max) {

C:
      max = number;
    }

    result.push(max);
  });

  return result;
};
