    int n=a.length();
    int m=b.length();
    for(int i=0;i<n;i++){
        a.insert(i,b);
        if(a.find(b)!=string::npos){
            return true;
        }
        a.erase(i,m);
    }
    return false;
}

B:
    int n = a.length();
    int m = b.length();
    for(int i = 0; i < n; i++) {
        string temp = a;
        for(int j = 0; j < m; j++) {
            temp.insert(i+j, b[j]);
        }
        if(temp.find(b) != string::npos) {
            return true;
        }
    }
    return false;
}

C:
    int n=a.length();
    int m=b.length();
    for(int i=0;i<n-m+1;i++){
        string temp=a.substr(i,m);
        if(temp==b || temp+b.substr(1,m-1)+temp[0] == b || temp+b.substr(2,m-2)+temp.substr(1,1)+temp[0] == b || temp+b.substr(3,m-3)+temp.substr(2,2)+temp.substr(1,1)+temp[0] == b || temp+b.substr(4,m-4)+temp.substr(3,3)+temp.substr(2,2)+temp.substr(1,1)+temp[0] == b || temp+b.substr(5,m-5)+temp.substr(4,4)+temp.substr(3,3)+temp.substr(2,2)+temp.substr(1,1)+temp[0] == b || temp+b.substr(6,m-6)+temp.substr(5,5)+temp.substr(4,4)+temp.substr(3,3)+temp.substr(2,2)+temp.substr(1,1)+temp[0] == b || temp+b.substr(7,m-7)+temp.substr(6,6)+temp.substr(5,5)+temp.substr(4,4)+temp.substr(3,3)+temp.substr(2,2)+temp.substr(1,1)+temp[0] == b){
            return true;
        }
    }
    return false;
}

D:
    int n = a.length();
    int m = b.length();
    for(int i = 0; i < n; i++) {
        if(a.substr(i, m) == b || a.substr(i, m) + a.substr(i+1