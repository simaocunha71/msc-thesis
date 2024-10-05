  var number_array = numbers.split(' ');
  number_array.sort((a, b) => {
    if (Number(a) < Number(b)) {
      return -1;
    } else if (Number(a) > Number(b)) {
      return 1;
    } else {
      return 0;
    }
  })
  return number_array.join(' ');
}



