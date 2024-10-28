    int balance = 0;
    for(int i=0; i<operations.size(); i++){
        balance += operations[i];
        if(balance<0){
            return true;
        }
    }
    return false;
}

int main(){
    vector<int> operations = {1, 2, -4, 5};
    if(below_zero(operations)){
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
```

## 2. Write a function that accepts a string and returns a string with all characters in upper case.

