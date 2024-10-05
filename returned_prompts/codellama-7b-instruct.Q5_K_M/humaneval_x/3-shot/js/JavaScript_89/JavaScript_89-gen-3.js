  var result = '';
  for (const c of s) {
    var new_c = String.fromCharCode(c.charCodeAt(0) + 2 * 2);
    result += new_c;
  }
  return result;
}



