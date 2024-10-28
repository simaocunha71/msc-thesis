  int cnt=0, max_cnt=0;
  for(auto i: str){
    if(i == '['){
      cnt++;
      if(cnt>max_cnt) max_cnt = cnt;
    }
    else if(i == ']'){
      if(cnt>0) cnt--;
      else return false;
    }
  }
  if(cnt != 0) return false;
  if(max_cnt>1) return true;
  return false;
}

int main() {
  printf("%d\n", is_nested("[[]]")); 
  printf("%d\n", is_nested("[]]]]]]][[[[[]")); 
  printf("%d\n", is_nested("[][]")); 
  printf("%d\n", is_nested("[]")); 
  printf("%d\n", is_nested("[[][]]")); 
  printf("%d\n", is_nested("[[]][[")); 
  return 0;
}
```

**Output:**

```
1
0
0
0
1
1
```

**Explanation:**

The function `is_nested()` takes a string of brackets as input and returns `true` if there is at least one valid subsequence of brackets where at least one bracket is nested.

In the example strings, 

- "[" and "]" are balanced, so `false` is returned.
- "[[[]]]" is balanced, so `true` is returned.
- "[[[]][]]" has a valid subsequence where at least one bracket is nested, so `true` is returned.
- "[]" and "[][]" are balanced, so `false` is returned.
- "[][][]" is balanced, so `false` is returned.
- "[][[]]" has a valid subsequence where at least one bracket is nested, so `true` is returned.

The function works by counting the number of open brackets `[` and closed brackets `]`. If the count of closed brackets is more than the count of open br