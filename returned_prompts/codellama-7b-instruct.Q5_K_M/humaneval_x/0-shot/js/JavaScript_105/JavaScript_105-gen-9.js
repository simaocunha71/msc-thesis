  const result = [];
  let str = '';
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      str += arr[i];
    }
  }
  str = str.split('').sort().reverse().join('');
  for (let i = 0; i < str.length; i++) {
    switch (str[i]) {
      case '1':
        result.push('One');
        break;
      case '2':
        result.push('Two');
        break;
      case '3':
        result.push('Three');
        break;
      case '4':
        result.push('Four');
        break;
      case '5':
        result.push('Five');
        break;
      case '6':
        result.push('Six');
        break;
      case '7':
        result.push('Seven');
        break;
      case '8':
        result.push('Eight');
        break;
      case '9':
        result.push('Nine');
        break;
    }
  }
  return result;


};
