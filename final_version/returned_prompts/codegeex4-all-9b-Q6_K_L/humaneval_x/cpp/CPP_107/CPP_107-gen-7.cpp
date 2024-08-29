    vector<int> res;
    for(int i=1;i<=n;i++){
        string s = to_string(i);
        string rev(s.rbegin(),s.rend());
        if(s==rev){
            if(i%2==0){
                res[0]+=1;
            }else{
                res[1]+=1;
            }
        }
    }
    return res;
}
B:
    vector<int> res(2,0);
    for(int i=1;i<=n;i++){
        string s = to_string(i);
        string rev(s.rbegin(),s.rend());
        if(s==rev){
            if(i%2==0){
                res[0]+=1;
            }else{
                res[1]+=1;
            }
        }
    }
    return res;
}
C:
    int even=0, odd=0;
    for(int i=1;i<=n;i++){
        string s = to_string(i);
        string rev(s.rbegin(),s.rend());
        if(s==rev){
            if(i%2==0){
                even+=1;
            }else{
                odd+=1;
            }
        }
    }
    return vector<int>{even,odd};
}
D:
    int even=0, odd=0;
    for(int i=1;i<=n;i++){
        string s = to_string(i);
        string rev(s.rbegin(),s.rend());
        if(s==rev){
            if(i%2==0){
                even++;
            }else{
                odd++;
            }
        }
    }
    return vector<int>{even,odd};
}
E:
    vector<int> res;
    res.push_back(0);
    res.push_back(0);
    for(int i=1;i<=n;i++){
        string s = to_string(i);
        string rev(s.rbegin(),s.rend());
        if(s==rev){
            if(i%2==0){
                res[0]+=1;
            }else{
                res[1]+=1;
            }
        }
    }
    return res;
}
F:
    vector<int> res(2,0);
    for(int i=1;i<=n;i++){
        string s = to_string(i);
        string rev(s.rbegin(),s.rend());
        if(s==rev){
            if(i%2==0){
                res[0]++;
            }else{
                res[1]++;
            }
        }
    }
    return res;
}
G:
    vector