    for (int i=0; i<l.size(); i++)
        l[i]++;
    return l;
}
int main(){
    vector<int> v1 = {1, 2, 3};
    vector<int> v2 = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    v1 = incr_list(v1);
    v2 = incr_list(v2);
    for(int i=0; i<v1.size(); i++)
        printf("%d ", v1[i]);
    printf("\n");
    for(int i=0; i<v2.size(); i++)
        printf("%d ", v2[i]);
    printf("\n");
    return 0;
}
```

## Problem 4:
Write a program in C++ that finds the maximum and minimum elements in the vector.

