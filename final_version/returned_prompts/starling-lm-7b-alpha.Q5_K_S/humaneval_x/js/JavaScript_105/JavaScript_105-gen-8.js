  const names = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
  };

  let result = [];
  let index = 0;
  while (index < arr.length && arr[index] < 0 || arr[index] > 9) {
    index += 1;
  }
  for (let i = index; i < arr.length; i++) {
    result.push(names[arr[i]]);
  }

  return result;
};



