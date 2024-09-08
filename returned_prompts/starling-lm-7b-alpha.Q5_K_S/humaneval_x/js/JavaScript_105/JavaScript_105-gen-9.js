  const arr1 = arr.filter((x) => x >= 1 && x <= 9);
  const arr2 = arr.filter((x) => x < 1 || x > 9);
  const arr3 = arr1.sort((a, b) => a - b);
  const arr4 = arr3.reverse();
  const arr5 = arr4.map((x) => {
    switch (x) {
      case 1: return 'One';
      case 2: return 'Two';
      case 3: return 'Three';
      case 4: return 'Four';
      case 5: return 'Five';
      case 6: return 'Six';
      case 7: return 'Seven';
      case 8: return 'Eight';
      case 9: return 'Nine';
      default: return 'No match';
    }
  });
  return arr5.filter((x) => x !== 'No match')
};



