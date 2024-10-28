  let result = [...s].filter(v => !c.includes(v)).join('');
  return [result, result === result.split('').reverse().join('')];
}



