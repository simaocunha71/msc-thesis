    map<string,string> mp;
    map<string,string>::iterator it;
    string res;
    string tmp;

    mp["zero"]="0";
    mp["one"]="1";
    mp["two"]="2";
    mp["three"]="3";
    mp["four"]="4";
    mp["five"]="5";
    mp["six"]="6";
    mp["seven"]="7";
    mp["eight"]="8";
    mp["nine"]="9";

    for (it=mp.begin();it!=mp.end();it++)
    {
        tmp=it->second;
        for (int i=0;i<numbers.length();i++)
        if (tmp==numbers.substr(i,tmp.length()))
        {
            res+=tmp;
            numbers=numbers.erase(i,tmp.length());
            i-=tmp.length();
        }
    }
    return res;
}




