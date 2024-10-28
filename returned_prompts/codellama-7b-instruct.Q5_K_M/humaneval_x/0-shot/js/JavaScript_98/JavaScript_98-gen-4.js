const countUpper = (s) => s.split('').filter((c, i) => c.toUpperCase() === c && i % 2 === 0).length;
