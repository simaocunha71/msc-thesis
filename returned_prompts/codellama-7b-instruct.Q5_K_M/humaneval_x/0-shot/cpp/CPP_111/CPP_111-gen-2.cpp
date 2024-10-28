    map<char,int> result;
    int max=0;
    for(int i=0;i<test.size();i++){
        if(result.find(test[i])==result.end()){
            result.insert(pair<char,int>(test[i],1));
        }
        else{
            result[test[i]]++;
        }
    }
    for(auto x:result){
        if(max<x.second){
            max=x.second;
        }
    }
    map<char,int>::iterator it=result.begin();
    for(;it!=result.end();it++){
        if(it->second==max){
            printf("%c %d\n",it->first,it->second);
        }
    }
    return result;
}
int main(){
    string test;
    getline(cin,test);
    map<char,int> result;
    result=histogram(test);
    return 0;
}
