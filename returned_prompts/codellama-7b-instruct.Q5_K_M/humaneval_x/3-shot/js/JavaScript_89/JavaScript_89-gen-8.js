  var encrypted = '';
  for (const c of s) {
    var current_char = c.charCodeAt(0);
    var new_char = current_char - 2 * 2;
    encrypted += String.fromCharCode(new_char);
  }

  return encrypted;
}



