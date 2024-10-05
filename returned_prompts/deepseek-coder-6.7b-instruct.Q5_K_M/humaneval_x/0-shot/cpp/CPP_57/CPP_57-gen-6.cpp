  bool inc = false;
  bool dec = false;
  for(int i = 0; i < l.size()-1; i++){
    if(l[i] < l[i+1])
      inc = true;
    if(l[i] > l[i+1])
      dec = true;
  }
  return inc && dec ? false : true;
}
int main(){
  vector<float> l1 = {1, 2, 4, 20};
  vector<float> l2 = {1, 20, 4, 10};
  vector<float> l3 = {4, 1, 0, -10};
  printf("%d\n", monotonic(l1));
  printf("%d\n", monotonic(l2));
  printf("%d\n", monotonic(l3));
  return 0;
}

//tests
/*
assert(monotonic({1, 2, 4, 20}))
assert(!monotonic({1, 20, 4, 10}))
assert(monotonic({4, 1, 0, -10}))
*/
```

## 6. Count the number of digits

```cpp
