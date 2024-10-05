  int i;
  char num[10];
  string s;
  for(i=0;i<=n;i++){
    sprintf(num, "%d", i);
    s += num;
    s += " ";
  }
  return s;
}
