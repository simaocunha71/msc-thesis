    vector<int> result;
    if (numbers.size() == 0)
        return result;
        
    result.push_back(numbers[0]);
    for (int i = 1; i < numbers.size(); i++){
        result.push_back(delimeter);
        result.push_back(numbers[i]);
    }
    return result;
}

int main(){
    vector<int> v = intersperse({1, 2, 3}, 4);
    for(int i = 0; i < v.size(); i++)
        printf("%d ", v[i]);
    return 0;
}
```

</details>

---

### 3.2.5 C++ Solutions

Here are C++ solutions for the problems.

<details>
<summary>Problem 1</summary>

