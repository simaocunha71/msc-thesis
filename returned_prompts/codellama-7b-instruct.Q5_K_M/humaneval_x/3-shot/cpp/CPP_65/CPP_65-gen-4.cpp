    string str=to_string(x);
    shift%=str.length();
    string result="";
    for (int i=0;i<str.length()-shift;i++)
    result+=str[i+shift];
    for (int i=0;i<shift;i++)
    result+=str[i];
    return result;
}



