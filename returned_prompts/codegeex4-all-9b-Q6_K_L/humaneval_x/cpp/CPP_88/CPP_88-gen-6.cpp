```cpp
vector<int> sort_array(vector<int> array){
    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 0){
        sort(array.rbegin(), array.rend());
    }
    else{
        sort(array.begin(), array.end());
    }
    return array;
}
```
B:
```cpp
vector<int> sort_array(vector<int> array){
    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 0){
        sort(array.begin(), array.end());
    }
    else{
        sort(array.rbegin(), array.rend());
    }
    return array;
}
```
C:
```cpp
vector<int> sort_array(vector<int> array){
    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 1){
        sort(array.rbegin(), array.rend());
    }
    else{
        sort(array.begin(), array.end());
    }
    return array;
}
```
D:
```cpp
vector<int> sort_array(vector<int> array){
    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 1){
        sort(array.begin(), array.end());
    }
    else{
        sort(array.rbegin(), array.rend());
    }
    return array;
}
```
E:
```cpp
vector<int> sort_array(vector<int> array){
    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 0){
        sort(array.begin(), array.end());
    }
    else{
        sort(array.rbegin(), array.rend());
    }
    return array;
}
```
F:
```cpp
vector<int> sort_array(vector<int> array){
    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 0){
        sort(array.rbegin(), array.rend());
    }
    else{
        sort(array.begin(), array.end());
    }
    return array;
}
```
F:
```