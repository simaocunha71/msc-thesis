  let result = [];
  for (const c of text) {
    if (c != ' ') {
      result.push(c);
    } else if (result.length > 1 && result[result.length - 2] == '_') {
      result.push('-');
    } else {
      result.push('_');
    }
  }
  return result.join('');
}



