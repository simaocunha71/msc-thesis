  const result = [];
  for (const n of numbers) {
    if (n >= 1 && n <= 9) {
      result.push(name(n));
    }
  }
  return result;
};

const arr = byLength(numbers);
const result = arr.reverse();
return nameNumber(result);
};



