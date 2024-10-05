  int a = 0, b = 0;
  for(int i = 0; i < lst.size(); i++)
  {
    if(lst[i] < 0 && lst[i] > a)
      a = lst[i];
    if(lst[i] > 0 && lst[i] < b || b == 0)
      b = lst[i];
  }
  if(a == 0 && b == 0)
  {
    return {0, 0};
  }
  else if(a == 0)
  {
    return {a, b};
  }
  else if(b == 0)
  {
    return {a, b};
  }
  else 
  {
    return {a, b};
  }
}

int main(){
  vector<int> lst = {2, 4, 1, 3, 5, 7};
  vector<int> result = largest_smallest_integers(lst);
  printf("%d %d", result[0], result[1]);
  return 0;
}

*/



















































































































































































































































