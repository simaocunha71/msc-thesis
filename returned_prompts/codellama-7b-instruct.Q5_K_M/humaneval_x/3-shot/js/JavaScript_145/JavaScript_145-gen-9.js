  const sorted = nums.slice().sort((a, b) => {
    const ad = a.toString().split('').map(x => parseInt(x)).reduce((acc, x) => acc + x, 0);
    const bd = b.toString().split('').map(x => parseInt(x)).reduce((acc, x) => acc + x, 0);
    if (ad == bd) return a - b;
    return ad - bd;
  });

  return sorted;
}



