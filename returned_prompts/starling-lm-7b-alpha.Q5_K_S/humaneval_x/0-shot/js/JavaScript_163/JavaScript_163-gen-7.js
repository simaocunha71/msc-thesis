
  const arrA = String(a).split('');
  const arrB = String(b).split('');
  let arr = [];
  let index = 0;

  while (index < arrA.length) {
    if (arrA[index] % 2 !== 0) {
      arr.push(Number(arrA[index]));
    }
    index++;
  }

  index = 0;
  while (index < arrB.length) {
    if (arrB[index] % 2 !== 0) {
     