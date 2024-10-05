    int i = 0;
    int j = arr.size() - 1;
    int count = 0;
    while(i < j){
        if(arr[i] != arr[j]){
            count++;
        }
        i++;
        j--;
    }
    return count;
}

int main()
{
    vector<int> arr = {1, 2, 3, 5, 4, 7, 9, 6};
    printf("%d\n", smallest_change(arr));
    return 0;
}
```

## 3. C++ Solution

```cpp
