for(int i=0;i<shift;i++){
    string str;
    str=to_string(x);
    str=str[str.length()-1]+str.substr(0,str.length()-1);
    x=atoi(str.c_str());
}
return to_string(x);
}

B:
string circular_shift(int x,int shift){
    string str=to_string(x);
    if(str.length()<shift){
        string str1;
        for(int i=str.length()-1;i>=0;i--){
            str1+=str[i];
        }
        return str1;
    }else{
    for(int i=0;i<shift;i++){
        char temp=str[str.length()-1];
        str=str.substr(0,str.length()-1);
        str+=temp;
    }
    }
    return str;
}

C:
string circular_shift(int x,int shift){
    string str=to_string(x);
    if(str.length()<shift){
        string str1;
        for(int i=str.length()-1;i>=0;i--){
            str1+=str[i];
        }
        return str1;
    }else{
        string str1=str.substr(str.length()-shift);
        str=str.substr(0,str.length()-shift);
        str+=str1;
    }
    return str;
}

D:
string circular_shift(int x,int shift){
    string str=to_string(x);
    if(str.length()<shift){
        string str1;
        for(int i=str.length()-1;i>=0;i--){
            str1+=str[i];
        }
        return str1;
    }else{
        string str1=str.substr(str.length()-shift);
        str=str.substr(0,str.length()-shift);
        str1+=str;
        str=str1;
    }
    return str;
}

E:
string circular_shift(int x,int shift){
    string str=to_string(x);
    if(str.length()<shift){
        string str1;
        for(int i=str.length()-1;i>=0;i--){
            str1+=str[i];
        }
        return str;
    }else{
        string str1=str.substr(str.length()-shift);
        str=str.substr(0,str.length()-shift);
        str1+=str;
        str=str1;
    }
    return str;
}

F:
string circular_shift(int x,int shift){
    string str=to_string(x);
    if(str.length()<shift){
        string str1;
        for(int i=str.length()-1;i>=0;i--){
            str1+=str[i];
        }
        return str1