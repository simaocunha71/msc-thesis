    sort(l.begin(),l.end());
    vector<int> a;
    for(int i=0;i<l.size()-1;i++){
        if(l[i]!=l[i+1]){
            a.push_back(l[i]);
        }
    }
    a.push_back(l[l.size()-1]);
    return a;
}
B:
    sort(l.begin(),l.end());
    vector<int> a;
    for(int i=0;i<l.size()-1;i++){
        if(l[i]!=l[i+1]){
            a.push_back(l[i]);
        }
    }
    return a;
C:
    sort(l.begin(),l.end());
    vector<int> a;
    for(int i=0;i<l.size();i++){
        if(i==0){
            a.push_back(l[i]);
        }
        else{
            if(l[i]!=l[i-1]){
                a.push_back(l[i]);
            }
        }
    }
    return a;
D:
    sort(l.begin(),l.end());
    vector<int> a;
    for(int i=0;i<l.size();i++){
        if(i==0){
            a.push_back(l[i]);
        }
        else{
            if(l[i]!=l[i+1]){
                a.push_back(l[i]);
            }
        }
    }
    return a;
E:
    sort(l.begin(),l.end());
    vector<int> a;
    for(int i=0;i<l.size();i++){
        if(i==0){
            a.push_back(l[i]);
        }
        else{
            if(l[i]!=a[a.size()-1]){
                a.push_back(l[i]);
            }
        }
    }
    return a;
F:
    sort(l.begin(),l.end());
    vector<int> a;
    for(int i=0;i<l.size();i++){
        if(i==0){
            a.push_back(l[i]);
        }
        else{
            if(l[i]!=a[a.size()-1] && l[i]!=a[a.size()-2]){
                a.push_back(l[i]);
            }
        }
    }
    return a;
G:
    sort(l.begin(),l.end());
    vector<int> a;
    for(int i=0;i<l.size();i++){
        if(i==0){
            a.push_back(l[i]);
        }
        else{
            if(l[i]!=a[a.size()-1] && l[i]!=a[a.size()-2] && l[i]!=a[a.size()-3]){
                a.push_back(l[i]);
            }
        }
    }
   