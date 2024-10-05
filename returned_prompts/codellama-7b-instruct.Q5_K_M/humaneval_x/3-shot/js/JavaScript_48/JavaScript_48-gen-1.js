  const text_array = text.split('');
  const reversed_array = text_array.reverse();

  for (var i = 0; i < text_array.length; i++) {
    if (text_array[i] != reversed_array[i]) {
      return false;
    }
  }

  return true;
}



