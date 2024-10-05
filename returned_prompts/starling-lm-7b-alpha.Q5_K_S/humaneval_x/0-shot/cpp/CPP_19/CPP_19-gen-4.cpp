    map<string,int> mp;
    mp["zero"]=0;
    mp["one"]=1;
    mp["two"]=2;
    mp["three"]=3;
    mp["four"]=4;
    mp["five"]=5;
    mp["six"]=6;
    mp["seven"]=7;
    mp["eight"]=8;
    mp["nine"]=9;
    int i=0;
    string s[10];
    while(i<10){
        char c;
        while((c=numbers[i])<=' ') i++;
        s[i]=string(1,c);
        i++;
    }
    for(int i=0;i<10;i++){
        for(int j=i+1;j<10;j++){
            if(mp[s[i]]>mp[s[j]]){
                swap(s[i],s[j]);
            }
        }
    }
    string res="";
    for(int i=0;i<10;i++) res+=s[i];
    return res;
}














































































































































































































































