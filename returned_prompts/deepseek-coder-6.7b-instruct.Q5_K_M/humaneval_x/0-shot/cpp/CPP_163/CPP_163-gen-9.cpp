    vector<int> even_nums;
    if(a>b){
        int c=a;
        a=b;
        b=c;
    }
    for(int i=a;i<=b;i++){
        if(i%2==0)
            even_nums.push_back(i);
    }
    return even_nums;
}

int main(){
    vector<int> res = generate_integers(2, 8);
    for(int i=0; i<res.size(); i++){
        printf("%d\n", res[i]);
    }
    return 0;
}
```

## 4. C++ 编程示例（使用 C++ 标准库）

```cpp
