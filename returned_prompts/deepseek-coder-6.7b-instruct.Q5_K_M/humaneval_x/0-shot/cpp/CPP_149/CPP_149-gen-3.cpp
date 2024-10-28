vector<string> result;

B:
for(int i=0;i<lst.size();i++){
    if(lst[i].size()%2==0){
        result.push_back(lst[i]);
    }
}

C:
sort(result.begin(), result.end(), [](string a, string b){
    if(a.size()==b.size()){
        return a<b;
    }
    return a.size()<b.size();
});

D:
return result;
}

int main() {
vector<string> lst = {"ab", "a", "aaa", "cd"};
vector<string> res = sorted_list_sum(lst);
for(int i=0;i<res.size();i++){
    printf("%s ",res[i].c_str());
}
return 0;
}

*/

