    int apples=0, oranges=0;
    string temp="";
    for(int i=0;i<s.length();i++){
        if(s[i]==' '||s[i]=='a'||s[i]=='n'||s[i]=='d'){
            if(temp=="apples"){
                apples=stoi(s.substr(0,i));
            }
            if(temp=="oranges"){
                oranges=stoi(s.substr(0,i));
            }
            temp="";
        }
        else{
            temp+=s[i];
        }
    }
    return n-apples-oranges;
}

