    for(int i=0; i<l.size(); i++){
        l[i]++;
    }
    return l;
}
int main(){
    vector<int> v1 = {1, 2, 3};
    vector<int> v2 = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> v1_incr = incr_list(v1);
    vector<int> v2_incr = incr_list(v2);
    for(int i=0; i<v1_incr.size(); i++){
        printf("%d ", v1_incr[i]);
    }
    printf("\n");
    for(int i=0; i<v2_incr.size(); i++){
        printf("%d ", v2_incr[i]);
    }
    printf("\n");
    return 0;
}
```

Output:
```
2 3 4 
6 4 6 3 4 4 10 1 124 
```

Note:
The problem is asking for C++. However, C++ is not as popular as Python or JavaScript in the programming community. Therefore, the above solution is in C++, but the problem is better suited for Python.

Below is the Python equivalent of the problem:

```python
def incr_vector(v):
    return [i+1 for i in v]

v1 = [1, 2, 3]
v2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]

print(incr_vector(v1))
print(incr_vector(v2))
```

Output:
```
[2, 3, 4]
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```

In this Python solution, we use a list comprehension to create a new list with each element of the original list incremented by 1.

**