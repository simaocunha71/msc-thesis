    string temp=b;
    bool check=false;
    int i;
    for (i=0;i<b.length();i++)
    {
        temp=b.substr(i)+b.substr(0,i);
        if (a.find(temp)!=string::npos){
            check=true;
            break;
        }
    }
    return check;
}


