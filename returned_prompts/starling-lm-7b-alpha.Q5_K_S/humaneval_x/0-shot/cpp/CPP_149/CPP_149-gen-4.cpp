    vector<string> tmp_list;
    for(int i=0;i<lst.size();i++){
        if(lst[i].size()%2==0) tmp_list.push_back(lst[i]);
    }
    sort(tmp_list.begin(),tmp_list.end());
    return tmp_list;
}
vector<string> vector_sort(vector<string> lst){
    vector<string> tmp_list;
    for(int i=0;i<lst.size();i++){
        if(lst[i].size()%2==1) tmp_list.push_back(lst[i]);
    }
    sort(tmp_list.begin(),tmp_list.end());
    return tmp_list;
}
int main(){
    vector<string> lst={"aa", "a", "aaa"};
    vector<string> ret=sorted_list_sum(lst);
    for(int i=0;i<ret.size();i++) printf("%s ",ret[i]);
    puts("");
    lst={"ab", "a", "aaa", "cd"};
    ret=vector_sort(lst);
    for(int i=0;i<ret.size();i++) printf("%s ",ret[i]);
    puts("");
    return 0;
}

*/

































































































































































































