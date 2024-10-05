    int sum = 0;
    for(unsigned int i=1; i<lst.size(); i+=2){
        if(lst[i] % 2 == 0){
            sum += lst[i];
        }
    }
    return sum;
}
int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}
```

## 3. 

```C++
