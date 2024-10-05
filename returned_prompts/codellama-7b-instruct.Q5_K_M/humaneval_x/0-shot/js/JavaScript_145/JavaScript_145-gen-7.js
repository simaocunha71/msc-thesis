const orderByPoints = (nums) => {
  // Sort the array based on the sum of its digits
  const sorted = nums.slice().sort((a, b) => {
    const sumA = a.toString().split("").reduce((acc, n) => acc + parseInt(n), 0);
    const sumB = b.toString().split("").reduce((acc, n) => acc + parseInt(n), 0);
    return sumA - sumB;
  });

  // Sort the array based on their index in original list
  return sorted.sort((a, b) => nums.indexOf(a) - nums.indexOf(b));
};

