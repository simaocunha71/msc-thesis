    map<char,int> m;
    for(int i = 0;i<test.size();i++){
        if(m.find(test[i])!=m.end()){
            m[test[i]]++;
        }else{
            m[test[i]] = 1;
        }
    }
    map<char,int>::iterator itr = m.end();
    itr--;
    int max = (*itr).second;
    while(m.begin()!=itr){
        if((*itr).second<max){
            m.erase(itr);
        }else if((*itr).second==max){
            (*itr).second = 0;
        }
        itr--;
    }
    return m;
}
int main(){
    string s;
    while(cin>>s){
        map<char,int> m = histogram(s);
        for(map<char,int>::iterator itr = m.begin();itr!=m.end();itr++){
            if(itr->second!=0){
                printf("{%c,%d}\n",(*itr).first,(*itr).second);
            }
        }
    }
    return 0;
}

*/




























































































































































































































