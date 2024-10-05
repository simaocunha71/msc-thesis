    vector<string> v;
    string x;
    int i;
    int j;
    int c;
    for (i=0;i<txt.length();i++){
        if (txt[i]==' ' || txt[i]==','){
            v.push_back(x);
            x="";
        }
        else
        x+=txt[i];
    }
    v.push_back(x);
    for (i=0;i<v.size();i++){
        c=0;
        for (j=0;j<v[i].length();j++){
            if ((ord(v[i][j])-ord('a'))%2!=0)
            c+=1;
        }
        v[i]=to_string(c);
    }
    return v;
}



