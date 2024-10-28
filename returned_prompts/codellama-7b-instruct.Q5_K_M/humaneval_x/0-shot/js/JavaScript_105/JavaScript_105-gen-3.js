  const sorted = arr.sort((a,b) => a - b);
  const reverse = sorted.reverse();
  const names = reverse.map(num => {
    if(num === 1) {
      return 'One';
    } else if (num === 2) {
      return 'Two';
    } else if (num === 3) {
      return 'Three';
    } else if (num === 4) {
      return 'Four';
    } else if (num === 5) {
      return 'Five';
    } else if (num === 6) {
      return 'Six';
    } else if (num === 7) {
      return 'Seven';
    } else if (num === 8) {
      return 'Eight';
    } else if (num === 9) {
      return 'Nine';
    } else {
      return 'Invalid'
    }
  });
  return names;
};

//test
const arr = [2,1,1,4,5,8,2,3];
console.log(byLength(arr));

/*
  