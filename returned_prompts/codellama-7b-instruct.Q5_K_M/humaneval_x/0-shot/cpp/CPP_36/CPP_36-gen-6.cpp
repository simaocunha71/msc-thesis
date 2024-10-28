  for(int i = 2; i < n; i++){
    if(i % 11 == 0 || i % 13 == 0)
      continue;
    if(i % 7 == 0)
      continue;
  }
  return 0;
}

