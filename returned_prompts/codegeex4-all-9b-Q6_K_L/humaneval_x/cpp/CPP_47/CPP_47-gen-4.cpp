    float a=l.size();
    float b=a/2;
    sort(l.begin(),l.end());
    if(a%2==0){
        float c=l[b-1]+l[b];
        return c/2;
    }
    else if(a%2==1){
        return l[b];
    }
    else{
        return 0;
    }
}

B:
float median(vector<float> l){
    sort(l.begin(),l.end());
    if(l.size()%2==0)
        return (l[l.size()/2]+l[l.size()/2-1])/2;
    else
        return l[l.size()/2];
}

C:
float median(vector<float> l){
    sort(l.begin(),l.end());
    return (l[(l.size()-1)/2]+l[l.size()/2])/2;
}

D:
float median(vector<float> l){
    sort(l.begin(),l.end());
    if(l.size()%2==0)
        return (l[l.size()/2]+l[l.size()/2-1])/2.0;
    else
        return l[l.size()/2];
}

E:
float median(vector<float> l){
    sort(l.begin(),l.end());
    return (l[(l.size()-1)/2]+l[l.size()/2])/2.0;
}

F:
float median(vector<float> l){
    sort(l.begin(),l.end());
    if(l.size()%2==0)
        return (l[l.size()/2]+l[l.size()/2-1])/2.0;
    else
        return l[(l.size()-1)/2];
}

G:
float median(vector<float> l){
    sort(l.begin(),l.end());
    return (l[l.size()/2]+l[l.size()/2-1])/2.0;
}

H:
float median(vector<float> l){
    sort(l.begin(),l.end());
    if(l.size()%2==0)
        return (l[l.size()/2]+l[l.size()/2-1])/2.0;
    else
        return l[l.size()/2-1];
}

I:
float median(vector<float> l){
    sort(l.begin(),l.end());
    if(l.size()%2==1)
        return (l[l.size()/2]+l[l.size()/2-1])/2.0;
    else
        return l[l.size()/2];
}

J:
float median(vector<float> l){
    sort(l.begin(),l.end());
    if(l.size()%