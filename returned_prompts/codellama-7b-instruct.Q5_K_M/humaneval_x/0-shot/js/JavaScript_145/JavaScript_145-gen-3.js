const orderByPoints = (nums) => {
  const sorted = nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    const sumB = b.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    return sumA - sumB;
  });
  const sortedIndexes = sorted.reduce((acc, cur, idx) => {
    acc[cur] = acc[cur] || [];
    acc[cur].push(idx);
    return acc;
  }, {});
  return nums.map(num => sortedIndexes[num].shift());
};
