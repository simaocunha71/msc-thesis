  let result = s.split('').filter(char => !c.includes(char));
  return [result.join(''), result.join('') === result.reverse().join('')];
}



