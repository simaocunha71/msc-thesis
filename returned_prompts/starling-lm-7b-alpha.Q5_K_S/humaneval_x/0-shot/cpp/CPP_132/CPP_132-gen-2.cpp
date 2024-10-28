    int len = str.length();
    int count = 0;
    for(int i=0;i<len;i++){
        if(str[i] == '[') count++;
        else if(str[i] == ']') count--;
        if(count < 0) return true;
    }
    return false;
}


int main(){
    string str = "[[]]";
    printf("%d",is_nested(str));
    return 0;
}











































































