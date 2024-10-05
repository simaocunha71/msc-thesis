  for  (let i = 0; i < n; i++) {
    if  (i % 11 === 0 || i % 13 === 0) {
      count += i.toString().split('').reduce((acc, cur)  =>  cur === '7' ? acc + 1 : acc, 0);
    }
  }

  return count;
}



