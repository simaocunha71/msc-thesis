  let newString = '';
  let sArray = s.split('');
  for (let i = 0; i < sArray.length; i++) {
    if (!c.includes(sArray[i])) {
      newString += sArray[i];
    }
  }
  return [newString, newString.split('').reverse().join('') === newString];
}  // or return [newString, newString === newString.split('').reverse().join('')];  // depending on how you want to handle the check



