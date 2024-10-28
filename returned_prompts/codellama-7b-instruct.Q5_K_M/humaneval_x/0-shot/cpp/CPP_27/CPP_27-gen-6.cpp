    /*
    for (int i = 0; i < str.size(); i++)
    {
        if(str[i] == ' ')
        {
            str[i] = ' ';
        }
        else
        {
            str[i] = str[i] ^ 0x20;
        }
    }
    return str;
    */
    int i = 0;
    while(i < str.length()){
        if (str[i] >= 'a' && str[i] <= 'z'){
            str[i] -= 32;
        }
        else if (str[i] >= 'A' && str[i] <= 'Z'){
            str[i] += 32;
        }
        i++;
    }
    return str;
}
int main(){
    string str = "hello world";
    cout << filp_case(str);
    return 0;
}
