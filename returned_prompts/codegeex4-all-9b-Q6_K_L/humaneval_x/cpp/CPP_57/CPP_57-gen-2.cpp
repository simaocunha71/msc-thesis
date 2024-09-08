bool increasing = true, decreasing = true;
for (int i = 1; i < l.size(); i++) {
	if (l[i] < l[i-1]) decreasing = false;
	if (l[i] > l[i-1]) increasing = false;
}
return increasing || decreasing;
}

B:
bool monotonic(vector<float> l){
    if(l.size()==0)
        return false;
    for(int i=0;i<l.size()-1;i++)
        if(l[i]>l[i+1])
            return false;
    return true;
}

C:
bool monotonic(vector<float> l){
    if(l.size()==0)
        return false;
    bool increasing = true;
    bool decreasing = true;
    for(int i=0;i<l.size()-1;i++)
    {
        if(l[i]>l[i+1])
            decreasing = false;
        if(l[i]<l[i+1])
            increasing = false;
    }
    return increasing || decreasing;
}

D:
bool monotonic(vector<float> l){
    if(l.size()==0)
        return false;
    for(int i=0;i<l.size()-1;i++)
    {
        if(l[i]<l[i+1])
            return false;
        if(l[i]>l[i+1])
            return false;
    }
    return true;
}

E:
bool monotonic(vector<float> l){
    if(l.size()==0)
        return false;
    for(int i=0;i<l.size()-1;i++)
    {
        if(l[i]<l[i+1])
            return false;
        if(l[i]>l[i+1])
            return false;
    }
    return true;
}

F:
bool monotonic(vector<float> l){
    if(l.size()==0)
        return false;
    for(int i=0;i<l.size()-1;i++)
    {
        if(l[i]>l[i+1])
            return false;
        if(l[i]<l[i+1])
            return false;
    }
    return true;
}

G:
bool monotonic(vector<float> l){
    if(l.size()==0)
        return false;
    for(int i=0;i<l.size()-1;i++)
    {
        if(l[i]<l[i+1])
            return false;
        if(l[i]>l[i+1])
            return false;
    }
    return true;
}

H:
bool monotonic(vector<float> l){
    if(l.size()==0)
        return false;
    for(int i=