```cpp
string change_base(int x,int base){
    string result;
    while(x){
        result=(char)(x%base+'0')+result;
        x/=base;
    }
    return result;
}
```