  var a_rotation = a;
  var b_rotation = b;
  var a_substring = false;

  while (a_rotation.length < b.length) {
    a_rotation += a_rotation;
  }

  for (var i = 0; i < a.length; i++) {
    if (a_rotation.includes(b)) {
      a_substring = true;
      break;
    }
  }

  return a_substring;
}



