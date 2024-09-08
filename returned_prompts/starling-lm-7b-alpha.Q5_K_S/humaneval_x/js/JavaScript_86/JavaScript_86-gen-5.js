  let arr = s.split('');
  for (let i = 0; i < arr.length; i++) {
    let index = arr.indexOf(arr[i]);
    if (index != i) {
      [arr[index], arr[i]] = [arr[i], arr[index]];
    }
  }
  return arr.join('');
}



