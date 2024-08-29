vector<int> ret;
vector<int> ret_sort;
for(int i=0;i<l.size();i++){
    if(i%3==0){
        ret.push_back(l[i]);
        ret_sort.push_back(l[i]);
    }
    else{
        ret.push_back(l[i]);
    }
}
sort(ret_sort.begin(),ret_sort.end());
for(int i=0;i<l.size();i++){
    if(i%3==0){
        ret[i]=ret_sort[i/3];
    }
}
return ret;
}