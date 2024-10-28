    return str;
}
int main(){
    string str = "hello";
    string r = filp_case(str);
    printf("%s\n", r.c_str());
}


Ans: C.
Explanation:
The problem statement asks to flip the case of all the characters in the string.
The solution is to convert the string to lower case if the string is all upper case and vice versa.







