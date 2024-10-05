  var result = '';

  if (shift > (x.toString().length - 1)) {
    result = x.toString().split('').reverse().join('');
  } else {
    var split_x = x.toString().split('');
    var shifted_x = split_x.splice(shift, split_x.length - shift).concat(split_x.splice(0, shift));
    result = shifted_x.join('');
  }

  return result;
}



