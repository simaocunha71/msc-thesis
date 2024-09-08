    if(s0.length()!=s1.length())
        return false;
    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    return s0==s1;
} 

B:
    if(s0.length()!=s1.length())
        return false;
    unordered_map<char,int> m0,m1;
    for(int i=0;i<s0.length();i++){
        m0[s0[i]]++;
        m1[s1[i]]++;
    }
    return m0==m1;
} 

C:
    if(s0.length()!=s1.length())
        return false;
    string s0sorted=s0;
    string s1sorted=s1;
    sort(s0sorted.begin(),s0sorted.end());
    sort(s1sorted.begin(),s1sorted.end());
    return s0sorted==s1sorted;
} 

D:
    if(s0.length()!=s1.length())
        return false;
    vector<int> v0(v0.length(),0),v1(v1.length(),0);
    for(int i=0;i<s0.length();i++){
        v0[s0[i]]++;
        v1[s1[i]]++;
    }
    return v0==v1;
} 

E:
    if(s0.length()!=s1.length())
        return false;
    for(int i=0;i<s0.length();i++){
        if(s0[i]!=s1[i])
            return false;
    }
    return true;
} 

F:
    if(s0.length()!=s1.length())
        return false;
    for(int i=0;i<s0.length();i++){
        for(int j=i+1;j<s0.length();j++){
            if(s0[i]==s0[j])
                return true;
        }
    }
    return false;
} 

G:
    if(s0.length()!=s1.length())
        return false;
    set<char> s0set,s1set;
    for(int i=0;i<s0.length();i++){
        s0set.insert(s0[i]);
        s1set.insert(s1[i]);
    }
    return s0set==s1set;
} 

H:
    if(s0.length()!=s1.length())
        return false;
    for(int i=0;i<s0.length();i++){
        if(s0.find(s1[i])!=string::npos)
            return true;
    }
    return false;
} 

I:
    if(s0.length()!=s1