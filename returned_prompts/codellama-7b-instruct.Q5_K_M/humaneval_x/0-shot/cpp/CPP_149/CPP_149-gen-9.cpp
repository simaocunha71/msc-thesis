    vector<string> sorted_list_sum;
    for(int i=0;i<lst.size();i++){
        if(lst[i].size()%2==0){
            sorted_list_sum.push_back(lst[i]);
        }
    }
    sort(sorted_list_sum.begin(),sorted_list_sum.end());
    return sorted_list_sum;
}

int main(){
    vector<string> lst = {"aa", "a", "aaa"};
    vector<string> res;
    res = sorted_list_sum(lst);
    for(int i=0;i<res.size();i++){
        printf("%s ",res[i].c_str());
    }
    return 0;
}
