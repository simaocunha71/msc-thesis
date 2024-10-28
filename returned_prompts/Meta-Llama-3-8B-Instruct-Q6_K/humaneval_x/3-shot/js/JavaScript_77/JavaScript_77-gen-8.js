  var cube_root = Math.cbrt(a);
  return Math.floor(cube_root) == cube_root;
} // note: Math.cbrt() is not supported in older browsers
// if you don't have Math.cbrt(), you can calculate cube_root manually
// const cube_root = Math.pow(a, 1.0 / 3.0);
// return Math.floor(cube_root) == cube_root;



