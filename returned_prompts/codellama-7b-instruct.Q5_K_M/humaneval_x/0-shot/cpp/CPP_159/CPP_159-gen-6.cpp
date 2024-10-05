  vector<int> a;

B:
  if(number >= need){
    a.push_back(number + remaining);
    a.push_back(0);
    return a;
  }

  else if(number < need){
    a.push_back(need);
    a.push_back(remaining - need);
    return a;
  }
}

int main(){
  int number, need, remaining;
  scanf("%d %d %d", &number, &need, &remaining);
  vector<int> res;
  res = eat(number, need, remaining);
  printf("%d %d", res[0], res[1]);
}
