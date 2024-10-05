
    bool isOpened = false;
    bool isClosed = false;
    int nested = 0;
    for(int i = 0; i < str.length(); i++){
        if(str[i] == '['){
            isOpened = true;
            nested++;
        }
        if(str[i] == ']'){
            isClosed = true;
            nested--;
        }
        if(nested < 0){
            return false;
        }
        if(isOpened && isClosed){
            return true;
        }
        isOpened = false;
        isClosed = false;
    }
    return false;
}
int main(){
    string str;
    cin>>str;
    if(is_nested(str)){
        printf("true");
    }else{
        printf("false");
    }
    return 0;
}
