    vector<int>v;
    for(int i=0;i<l1.size();i++){
        for(int j=0;j<l2.size();j++){
            if(l1[i]==l2[j]){
                v.push_back(l1[i]);
                break;
            }
        }
    }
    sort(v.begin(),v.end());
    v.erase(unique(v.begin(),v.end()),v.end());
    return v;
}


int main(){
    vector<int>v1={1, 4, 3, 34, 653, 2, 5};
    vector<int>v2={5, 7, 1, 5, 9, 653, 121};
    vector<int>v=common(v1,v2);
    for(int i=0;i<v.size();i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;
    return 0;
}
