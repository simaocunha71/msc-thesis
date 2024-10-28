const oddCount = (lst) => {
  let odd = 0;
  for(let i = 0; i < lst.length; i++) {
    let num = lst[i];
    for(let j = 0; j < num.length; j++) {
      if(num[j] % 2 === 1) {
        odd++;
      }
    }
  }
  return odd;
}
