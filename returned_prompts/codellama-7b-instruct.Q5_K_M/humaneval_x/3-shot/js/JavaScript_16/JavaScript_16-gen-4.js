  var char_list = string.toLowerCase().split('');
  var result = [];
  for (const c of char_list) {
    if (!result.includes(c)) {
      result.push(c);
    }
  }
  return result.length;
}



