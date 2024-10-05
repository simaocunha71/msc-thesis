    int lst1size = lst1.size();
    int lst2size = lst2.size();
    int lst1sum=0,lst2sum=0;
    for(int i=0;i<lst1size;i++){
        lst1sum+=lst1[i].size();
    }
    for(int i=0;i<lst2size;i++){
        lst2sum+=lst2[i].size();
    }
    if(lst1sum<lst2sum){
        return lst1;
    }
    else if(lst1sum>lst2sum){
        return lst2;
    }
    else{
        for(int i=0;i<lst1size;i++){
            if(lst1[i].size()<lst2[i].size()){
                return lst1;
            }
        }
        for(int i=0;i<lst2size;i++){
            if(lst2[i].size()<lst1[i].size()){
                return lst2;
            }
        }
    }
    return lst1;
}
int main(){
    vector<string> v1={"a","b","c"};
    vector<string> v2={"a","b","c","d"};
    vector<string> v3={"a","b","c","d","e"};
    vector<string> v4={"a","b"};
    vector<string> v5={"a"};
    vector<string> v6={"a"};
    vector<string> v7={"a","b"};
    printf("%s\n",total_match(v1,v2).c_str());
    printf("%s\n",total_match(v1,v3).c_str());
    printf("%s\n",total_match(v4,v5).c_str());
    printf("%s\n",total_match(v4,v6).c_str());
    printf("%s\n",total_match(v5,v6).c_str());
    printf("%s\n",total_match