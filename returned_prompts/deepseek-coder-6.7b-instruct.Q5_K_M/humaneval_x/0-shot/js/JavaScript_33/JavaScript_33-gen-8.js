  const l_prime = [...l];

  l.forEach((_, i) => {
    if (i % 3 === 0) {
      l_prime[i] = l.filter((_, j) => j % 3 === 0).sort((a, b) => a - b)[i / 3 | 0];
    }
  });

  return l_prime;
};

console.log(sortThird([1, 2, 3]));
console.log(sortThird([5, 6, 3, 4, 8, 9, 2]));

