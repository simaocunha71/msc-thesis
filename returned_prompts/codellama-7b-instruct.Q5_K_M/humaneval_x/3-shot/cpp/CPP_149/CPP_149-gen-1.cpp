    sort(lst.begin(),lst.end(),[](string a,string b){
        return (a.length() > b.length()) || (a.length() == b.length() && a < b);
    });

    return lst;
}



