int digits(int n){
    string s = to_string(n);
    int product = 1;
    bool all_even = true;
    for(char c : s){
        int digit = c - '0';
        if(digit % 2 != 0){
            product *= digit;
            all_even = false;
        }
    }
    return all_even ? 0 : product;
}

B:
int digits(int n){
    string s = to_string(n);
    int product = 1;
    for(char c : s){
        int digit = c - '0';
        if(digit % 2 != 0){
            product *= digit;
        }
    }
    return product;
}

C:
int digits(int n){
    string s = to_string(n);
    int product = 1;
    bool all_even = true;
    for(char c : s){
        int digit = c - '0';
        if(digit % 2 != 0){
            product *= digit;
        }
        if(digit % 2 == 0){
            all_even = false;
        }
    }
    return all_even ? 0 : product;
}

D:
int digits(int n){
    string s = to_string(n);
    int product = 1;
    bool all_even = true;
    for(char c : s){
        int digit = c - '0';
        if(digit % 2 == 0){
            all_even = false;
        }
        else{
            product *= digit;
        }
    }
    return all_even ? 0 : product;
}

E:
int digits(int n){
    string s = to_string(n);
    int product = 1;
    for(char c : s){
        int digit = c - '0';
        if(digit % 2 == 0){
            product *= digit;
        }
    }
    return product;
}
请问哪个函数是正确的，能正确解决问题吗？

选项C是正确的。它首先初始化一个变量`product`为1，然后检查字符串中的每个数字。如果数字是奇数，它将乘以`product`。如果数字是偶数，它将设置`all_even`为false。最后，如果`all_even`仍然为true（意味着所有数字都是偶数），函数返回0，否则返回`product`。

其他选项的问题在于它们在遇到偶数时没有正确地处理`all_even`变量。例如，选项A和B在遇到偶数