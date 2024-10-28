    vector<int> ans;
    while(lst.size() > 0){
        int min = 100000000;
        int max = 0;
        for(int i = 0; i < lst.size(); i++){
            if(lst[i] < min) min = lst[i];
            if(lst[i] > max) max = lst[i];
        }
        for(int i = 0; i < lst.size(); i++){
            if(lst[i] != max) continue;
            lst.erase(lst.begin() + i);
            ans.push_back(max);
            break;
        }
        for(int i = 0; i < lst.size(); i++){
            if(lst[i] != min) continue;
            lst.erase(lst.begin() + i);
            ans.push_back(min);
            break;
        }
    }
    return ans;
}
int main(){
    vector<int> t = {1, 2, 3, 4};
    vector<int> ans = strange_sort_list(t);
    for(int i = 0; i < ans.size(); i++) printf("%d ", ans[i]);
    return 0;
}








































































































































































































