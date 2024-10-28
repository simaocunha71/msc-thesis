    if(x%2==0){
        if(x>=y){
            return x;
        }
        else{
            return -1;
        }
    }
    else{
        x++;
        if(x>y){
            return -1;
        }
        else{
            return x;
        }
    }

}
int main() {
    printf("%d\n", choose_num(12, 15)); // expected output 14
    printf("%d\n", choose_num(13, 12)); // expected output -1
    return 0;
}
```

This function works by first checking if x is even. If it is, then it checks if x is greater than or equal to y. If both conditions are met, it returns x. If x is not even, it increments x by one and checks if x is greater than y. If it is, it returns -1. Otherwise, it returns x.

Note: This code uses C++ syntax, and you need to use a C++ compiler to run it.


