  let result = [...s].filter(e => !c.includes(e)).join('');
  let check = result.split('').reverse().join('') === result;
  return [result, check];
}



