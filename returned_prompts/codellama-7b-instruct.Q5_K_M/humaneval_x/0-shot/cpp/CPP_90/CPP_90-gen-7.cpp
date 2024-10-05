    if(lst.size()<=1)
        return -1;
    vector<int>::iterator it;
    for(it=lst.begin();it!=lst.end();it++){
        vector<int>::iterator it1;
        for(it1=lst.begin();it1!=lst.end();it1++){
            if(*it1<*it)
                goto B;
        }
    }
    goto C;
B:
    vector<int>::iterator it2;
    for(it2=lst.begin();it2!=lst.end();it2++){
        if(*it2==*it)
            goto C;
    }
C:
    if(it2!=lst.end()){
        return *it2;
    }
    else{
        return -1;
    }
}
int main(){
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    printf("%d",next_smallest(v));
    return 0;
}
