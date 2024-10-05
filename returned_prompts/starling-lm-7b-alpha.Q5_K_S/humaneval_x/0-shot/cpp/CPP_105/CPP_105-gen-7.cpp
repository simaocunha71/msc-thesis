    vector<int> tmp_arr;
    for(int i=0;i<arr.size();i++)
        if(arr[i]>=1&&arr[i]<=9)
            tmp_arr.push_back(arr[i]);
    sort(tmp_arr.begin(),tmp_arr.end());
    reverse(tmp_arr.begin(),tmp_arr.end());
    vector<string> name;
    map<int,string> mp;
    mp[1]="One";
    mp[2]="Two";
    mp[3]="Three";
    mp[4]="Four";
    mp[5]="Five";
    mp[6]="Six";
    mp[7]="Seven";
    mp[8]="Eight";
    mp[9]="Nine";
    for(int i=0;i<tmp_arr.size();i++)
        name.push_back(mp[tmp_arr[i]]);
    return name;
}
int main(){
    vector<int> arr={1, -1 , 55};
    vector<string> res=by_length(arr);
    for(int i=0;i<res.size();i++)
        printf("%s ",res[i].c_str());
    printf("\n");
}







































































































































































































