  return nums.sort((a, b) => {
    const sumA = sumDigits(a);
    const sumB = sumDigits(b);
    if (sumA !== sumB) {
      return sumA < sumB ? -1 : 1;
    } else {
      return a < b ? -1 : 1;
    }
  });
}



