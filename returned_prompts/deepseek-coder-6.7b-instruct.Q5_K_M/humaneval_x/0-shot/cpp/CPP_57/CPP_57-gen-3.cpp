    for(int i=0; i<l.size()-1; i++){
        if(l[i]>l[i+1])
            return false;
    }
    return true;
}

int main()
{
    vector<float> v1={1, 2, 4, 20};
    vector<float> v2={1, 20, 4, 10};
    vector<float> v3={4, 1, 0, -10};
    printf("%d\n", monotonic(v1));
    printf("%d\n", monotonic(v2));
    printf("%d\n", monotonic(v3));
    return 0;
}
```

### Output:
```
1
0
1
```

## 7. Program to find the second smallest and second largest element in an array.

```C++
