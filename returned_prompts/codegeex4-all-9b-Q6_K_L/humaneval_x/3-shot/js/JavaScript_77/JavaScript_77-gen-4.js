  if (a == 0) return true;

  let cube_root = Math.pow(a, 1 / 3);
  let int_cube_root = Math.floor(cube_root);

  return cube_root == int_cube_root * int_cube_root * int_cube_root;
}