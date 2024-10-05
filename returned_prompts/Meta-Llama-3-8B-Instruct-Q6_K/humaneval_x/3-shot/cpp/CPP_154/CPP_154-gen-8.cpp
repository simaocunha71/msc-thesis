    string b1=b;
    for(int i=0;i<b.size();i++){
        b1=b1.substr(1)+b1[0];
        if(a.find(b1)!=string::npos)
            return true;
    }
    return false;
}  



