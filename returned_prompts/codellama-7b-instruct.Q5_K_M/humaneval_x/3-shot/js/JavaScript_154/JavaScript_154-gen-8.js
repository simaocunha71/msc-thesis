  var flag = false;
  var b_rot = [b, b.slice(1) + b[0], b.slice(2) + b[1] + b[0]];
  for (var i = 0; i < b_rot.length; i++) {
    if (a.includes(b_rot[i])) {
      flag = true;
      break;
    }
  }
  return flag;
}



