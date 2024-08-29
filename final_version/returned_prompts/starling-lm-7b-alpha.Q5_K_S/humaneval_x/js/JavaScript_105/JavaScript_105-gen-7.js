  const arr1 = arr.sort((a, b) => {
    if (a === b) return 0;
    if (a === 1 || b === 1) return a - b;
    return 0;
  });
  const arr2 = arr1.reverse();
  const arr3 = arr2.map((num) => {
    switch (num) {
      case 1: return 'One';
      case 2: return 'Two';
      case 3: return 'Three';
      case 4: return 'Four';
      case 5: return 'Five';
      case 6: return 'Six';
      case 7: return 'Seven';
      case 8: return 'Eight';
      case 9: return 'Nine';
      default: return '';
    }
  });
  return arr3.filter((name) => name !== '');
};



