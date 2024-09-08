    vector<int> v;
    for(int i=0; i<l.size(); i++){
        bool duplicate = false;
        for(int j = 0; j < v.size(); j++){
            if(v[j] == l[i]){
                duplicate = true;
                break;
            }
        }
        if(!duplicate) v.push_back(l[i]);
    }
    sort(v.begin(), v.end());
    return v;
}
int main()
{
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> res = unique(l);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

