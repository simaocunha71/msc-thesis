    if (strings.size()==0) return None;
    string longest = strings[0];
    for(int i=1; i<strings.size(); i++){
        if(strings[i].size() > longest.size()){
            longest = strings[i];
        }
    }
    return longest;
}
int main(){
    vector<string> s = {"a", "bb", "ccc"};
    cout<<longest(s)<<endl;
    return 0;
}
