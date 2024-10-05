  let filteredString = s.replace(new RegExp(c, 'g'), '');
  let reversedString = filteredString.split('').reverse().join('');
  return [filteredString, filteredString == reversedString];
}