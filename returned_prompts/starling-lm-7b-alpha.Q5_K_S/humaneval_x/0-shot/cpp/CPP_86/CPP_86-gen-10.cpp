    int l = s.size();
    char ch[l];
    for(int i = 0; i < l; i++)
        ch[i] = s[i];
    for(int i = 0; i < l; i++)
    {
        int min = i;
        for(int j = i + 1; j < l; j++)
        {
            if(ch[j] < ch[min])
                min = j;
        }
        char tmp = ch[min];
        ch[min] = ch[i];
        ch[i] = tmp;
    }
    for(int i = 0; i < l; i++)
        if(ch[i] == ' ')
        {
            s[i] = ' ';
            continue;
        }
        else
        {
            s[i] = ch[i];
        }
    return s;
}

int main(){
    string s;
    while(cin>>s){
        printf("%s\n",anti_shuffle(s).c_str());
    }
    return 0;
}





















































































































































































































































