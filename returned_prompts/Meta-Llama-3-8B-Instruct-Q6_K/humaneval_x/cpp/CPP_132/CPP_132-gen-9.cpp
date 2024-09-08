    int count = 0;
    for(int i=0; i<str.length(); i++){
        if(str[i] == '['){
            count++;
        }
        else if(str[i] == ']'){
            if(count == 0) return false;
            count--;
        }
    }
    return count > 0;
}

int main(){
    string str1 = "[[]]";
    string str2 = "[]]]]]]][[[[[]";
    string str3 = "[][]";
    string str4 = "[]";
    string str5 = "[[][]]";
    string str6 = "[[]][[";
    cout << is_nested(str1) << endl;
    cout << is_nested(str2) << endl;
    cout << is_nested(str3) << endl;
    cout << is_nested(str4) << endl;
    cout << is_nested(str5) << endl;
    cout << is_nested(str6) << endl;
    return 0;
}