  var root = Math.pow(a, 1/3);
  var root_squared = Math.pow(root, 2);
  var diff = root_squared - a;
  return diff < 0.001;
}



