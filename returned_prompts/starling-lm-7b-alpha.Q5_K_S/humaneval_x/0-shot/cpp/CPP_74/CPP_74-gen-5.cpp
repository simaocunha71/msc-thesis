    if(lst1.size()<lst2.size())return lst1;
    else if(lst1.size()>lst2.size())return lst2;
    else{
        int cnt=0;
        for(int i=0;i<lst1.size();i++){
            cnt+=lst1[i].size();
        }
        int cnt1=0;
        for(int i=0;i<lst2.size();i++){
            cnt1+=lst2[i].size();
        }
        if(cnt<cnt1)return lst1;
        else if(cnt>cnt1)return lst2;
        else{
            for(int i=0;i<lst1.size();i++){
                if(lst1[i].size()<lst2[i].size()){
                    return lst1;
                }
                else if(lst1[i].size()>lst2[i].size()){
                    return lst2;
                }
            }
        }
        return lst1;
    }
}
int main(){
    vector<string> lst1={"123","456"};
    vector<string> lst2={"1","2","3","4","5"};
    printf("%s",total_match(lst1,lst2).size()?"1":"0");
    return 0;
}














































































































































































