    string s2;
    s2=s0;
    sort(s2.begin(),s2.end());
    s1=s1;
    sort(s1.begin(),s1.end());
    if(s2==s1)return true;
    else return false;
}

int main(){
    string s0,s1;
    while(cin>>s0>>s1)printf("%s\n",same_chars(s0,s1)?"true":"false");
    return 0;
}














*/
    return 0;
}


```