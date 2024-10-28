  var palindromic_suffix = '';

  for (let i = string.length - 1; i >= 0; i--) {
    if (string.substring(i) == string.substring(i).split('').reverse().join('')) {
      palindromic_suffix = string.substring(i);
      break;
    }
  }

  return string + palindromic_suffix.split('').reverse().join('');
}



