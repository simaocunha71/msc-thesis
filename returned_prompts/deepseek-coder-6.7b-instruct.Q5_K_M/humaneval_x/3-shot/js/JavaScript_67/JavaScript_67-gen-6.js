  const applesOranges ​= s.match(/\d+/g);
  const apples ​= Number(applesOranges[0]);
  const oranges ​= Number(applesOranges[1]);
  return n - apples - oranges;
}



