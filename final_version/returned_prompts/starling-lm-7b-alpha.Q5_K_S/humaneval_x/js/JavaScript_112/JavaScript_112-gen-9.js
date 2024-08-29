  let result = s.replace(new RegExp(c, 'g'), '');

  return [result, result === result.split('').reverse().join('')];
}



