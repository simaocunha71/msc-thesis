    sort(arr.begin(),arr.end());

    vector<int> tmp;
    for(int i:arr){
        if(i<0||i>9) continue;
        tmp.push_back(i);
    }
    reverse(tmp.begin(),tmp.end());
    vector<string> ret;
    map<int,string> mp={
        {1,"One"},
        {2,"Two"},
        {3,"Three"},
        {4,"Four"},
        {5,"Five"},
        {6,"Six"},
        {7,"Seven"},
        {8,"Eight"},
        {9,"Nine"},
    };
    for(int i:tmp) ret.push_back(mp[i]);
    return ret;
}
int main(){
    vector<int> arr={2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> ret=by_length(arr);
    for(string str:ret) printf("%s ",str.c_str());
    return 0;
}



























































































































































































































































