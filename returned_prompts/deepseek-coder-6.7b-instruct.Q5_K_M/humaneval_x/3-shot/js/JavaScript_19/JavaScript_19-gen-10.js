  const numberNames = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
  return numbers.split(' ').sort((a, b) => numberNames.indexOf(a) - numberNames.indexOf(b)).join(' ');
}



