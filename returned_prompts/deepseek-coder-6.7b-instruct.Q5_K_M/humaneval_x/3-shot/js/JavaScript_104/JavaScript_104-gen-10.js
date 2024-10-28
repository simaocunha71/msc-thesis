  let res = [];

  for(let i of x) {
    if(!(i.toString().match(/[02468]/))) {
      res.push(i);
    }
  }

  return res.sort((a, b) => a - b);
}



