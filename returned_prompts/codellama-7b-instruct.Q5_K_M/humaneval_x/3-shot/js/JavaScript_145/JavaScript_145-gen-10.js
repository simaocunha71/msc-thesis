  nums.sort((a, b) => {
    if (a > b) {
      return 1;
    } else if (a < b) {
      return -1;
    } else {
      return a - b;
    }
  });

  return nums;
}



