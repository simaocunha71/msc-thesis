  return numbers.reduce((acc, current) => {
    return acc.concat([current, delimeter]);
  }, []).slice(0, -1);
};

console.log(intersperse([1, 2, 3], 4));




// ----------------
// Solution 2
// ----------------

