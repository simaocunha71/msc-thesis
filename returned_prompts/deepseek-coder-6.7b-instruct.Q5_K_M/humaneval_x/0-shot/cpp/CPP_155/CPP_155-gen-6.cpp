  int count_odd=0, count_even=0;
  num = abs(num);
  while(num>0){
    if((num%10)%2==0)
      count_even++;
    else
      count_odd++;
    num = num/10;
  }
  return vector<int>{count_even, count_odd};
}

int main(){
  vector<int> result = even_odd_count(-12);
  printf("Even: %d, Odd: %d\n", result[0], result[1]);
  result = even_odd_count(123);
  printf("Even: %d, Odd: %d\n", result[0], result[1]);
  return 0;
}
```


## Possibly Mistaken question

