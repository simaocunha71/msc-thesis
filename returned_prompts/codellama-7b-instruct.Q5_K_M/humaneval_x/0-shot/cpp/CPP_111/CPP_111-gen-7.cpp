    map<char,int> result;
    int max=0;
    char temp;
    for(int i=0;i<test.size();i++){
        if(result.find(test[i])==result.end()){
            result.insert(pair<char,int>(test[i],1));
        }
        else{
            result[test[i]]++;
        }
        if(result[test[i]]>max){
            max=result[test[i]];
            temp=test[i];
        }
    }
    if(max==0){
        return result;
    }
    else{
        for(int i=0;i<test.size();i++){
            if(result[test[i]]==max){
                result.insert(pair<char,int>(test[i],max));
            }
        }
    }
    return result;
}
int main(){
    map<char,int> result=histogram("a b c a b");
    for(map<char,int>::iterator it=result.begin();it!=result.end();it++){
        printf("%c %d\n",it->first,it->second);
    }
    return 0;
}
