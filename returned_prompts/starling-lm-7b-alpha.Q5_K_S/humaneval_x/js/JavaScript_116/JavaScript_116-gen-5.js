  const helper = (num, bitCount) => {
    if (num === 0) return [0, bitCount];
    return helper(num >> 1, bitCount + 1);
  };

  return arr.sort((a, b) => {
    const [one1, count1] = helper(a);
    const [one2, count2] = helper(b);
    if (count1 !== count2) return count1 - count2;
    return one1 - one2;
  });
}



