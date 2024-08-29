  const string_length = string.length;

  if (string_length == 1) {
    return true;
  }

  for (let i = 2; i < string_length; i++) {
    if (string_length % i == 0) {
      return false;
    }
  }
  return true;
}



