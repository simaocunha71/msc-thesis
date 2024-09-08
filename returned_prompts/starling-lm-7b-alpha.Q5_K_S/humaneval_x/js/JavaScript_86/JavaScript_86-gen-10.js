  let result = [];
  let ascii_values = Array.from(s);

  for (const c of ascii_values) {
    let index = ascii_values.indexOf(c);
    result.push(ascii_values.splice(index, 1).join(''));
  }

  return result.join('');
}



