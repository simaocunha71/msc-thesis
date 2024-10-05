    int apples=0,oranges=0;
    string temp="";
    for(char c:s){
        if(c==' ')continue;
        if(isdigit(c))temp+=c;
        else{
            if(temp.size()) {
                if(temp=="apples")apples=stoi(temp);
                else if(temp=="oranges")oranges=stoi(temp);
                temp="";
            }
        }
    }
    if(temp.size()) {
        if(temp=="apples")apples=stoi(temp);
        else if(temp=="oranges")oranges=stoi(temp);
    }
    int fruits=apples+oranges;
    return n-fruits;
}


