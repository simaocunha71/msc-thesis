```cpp
int sum=0,prod=1;
for(int i=0;i<arr.size();i++){
    sum+=abs(arr[i]);
    if(arr[i]<0)prod=-prod;
}
return prod*sum;
}
```
