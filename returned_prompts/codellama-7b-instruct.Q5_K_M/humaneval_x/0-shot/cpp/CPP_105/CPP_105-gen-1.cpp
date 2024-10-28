    vector<int> result;
    vector<string> names;
    map<int,string> m={
        {1,"One"},
        {2,"Two"},
        {3,"Three"},
        {4,"Four"},
        {5,"Five"},
        {6,"Six"},
        {7,"Seven"},
        {8,"Eight"},
        {9,"Nine"}
    };
    for(int x:arr){
        if(x>9 || x<1)
            continue;
        else{
            result.push_back(x);
            names.push_back(m[x]);
        }
    }
    sort(result.begin(),result.end());
    reverse(result.begin(),result.end());
    for(int i=0;i<result.size();i++){
        cout<<names[i]<<endl;
    }
    return names;
}
int main(){
    vector<int> arr={2,1,1,4,5,8,2,3};
    vector<string> res=by_length(arr);
    return 0;
}
*/
