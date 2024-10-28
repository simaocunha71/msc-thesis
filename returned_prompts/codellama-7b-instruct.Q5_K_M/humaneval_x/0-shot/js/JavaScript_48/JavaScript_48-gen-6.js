  // convert to lower case and remove all non-alphanumeric characters
  text = text.toLowerCase().replace(/\W/g, '');

  // check if string is the same backwards and forwards
  return text === text.split('').reverse().join('');
}

