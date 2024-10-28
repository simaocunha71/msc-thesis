  // Solution 1 - math
  const iscube = (a) => {
    return Math.pow(a, 1/3) % 1 === 0;
  };

  // Solution 2 - loop
  const iscube = (a) => {
    for (let i = 0; i < a; i++) {
      if (Math.pow(i, 3) === a) return true;
    }
    return false;
  };

  // Solution 3 - recursion
  const iscube = (a) => {
    if (a === 0) return true;
    if (Math.floor(Math.pow(a, 1/3)) ** 3 === a) return true;
    return false;
  };

  // Solution 4 - no loop
  const iscube = (a) => {
    return (Math.sqrt(Math.sqrt(a)) % 1 === 0) && (Math.cbrt(a) % 1 === 0);
  };

  // Solution 5 - no loop
  const iscube = (a) => {
    return (Math.pow(Math.sqrt(a), 2) === a) && (Math.pow(a, 1/3) === Math.pow(Math.sqrt(a), 2) / Math.sqrt(a));
  };

  // Solution 6 - no loop
  const iscube = (a) => {
    return (Math.pow(Math.cbrt(a), 3) === a) && (Math.cbrt(a) % 1 === 0);
  };

  // Solution 7 - no loop
  const iscube = (a) => {
    return (Math.pow(Math.pow(Math.pow(a, 1/3), 3), 3) === a) && (Math.pow(Math.pow(Math.pow(a, 1/3), 3), 1/3) % 1 === 0);
  };

  // Solution 8 - no loop
  const iscube = (a) => {
    return (Math.pow(Math.pow