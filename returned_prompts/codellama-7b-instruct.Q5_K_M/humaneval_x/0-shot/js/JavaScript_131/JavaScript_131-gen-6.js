  //
  if(n === 0) return 0;
  const num = n.toString();
  const arr = num.split('');
  const result = [];
  for(let i = 0; i < arr.length; i++) {
    if(arr[i] % 2 !== 0) {
      result.push(arr[i]);
    }
  }
  return result.reduce((total, num) => total*num, 1);

}

const digits = (n) => {

B:
  //
  if(n === 0) return 0;
  const num = n.toString();
  const arr = num.split('');
  const result = [];
  for(let i = 0; i < arr.length; i++) {
    if(arr[i] % 2 === 0) {
      result.push(arr[i]);
    }
  }
  return result.reduce((total, num) => total*num, 1);

}

const digits = (n) => {

C:
  //
  if(n === 0) return 0;
  const num = n.toString();
  const arr = num.split('');
  const result = [];
  for(let i = 0; i < arr.length; i++) {
    if(arr[i] % 2 !== 0) {
      result.push(arr[i]);
    }
  }
  return result.reduce((total, num) => total*num, 1);

}
