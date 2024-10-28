    string temp;
    for(int i=0;i<b.length();i++){
        temp=b.substr(i)+b.substr(0,i);
        if(a.find(temp)!=string::npos)
            return true;
    }
    return false;
}


