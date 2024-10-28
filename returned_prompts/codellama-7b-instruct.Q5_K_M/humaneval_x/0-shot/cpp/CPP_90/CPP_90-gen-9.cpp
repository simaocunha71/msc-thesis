    if(lst.size()<2){
        return -1;
    }
    sort(lst.begin(),lst.end());
    vector<int>::iterator it;
    it=find(lst.begin(),lst.end(),lst[1]);
    if(it==lst.end()){
        return -1;
    }
    else{
        return *(it+1);
    }
}


