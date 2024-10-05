  return numbers.split(' ').sort((a, b) => {
    return parseInt(a) - parseInt(b);
  }).join(' ');
}



