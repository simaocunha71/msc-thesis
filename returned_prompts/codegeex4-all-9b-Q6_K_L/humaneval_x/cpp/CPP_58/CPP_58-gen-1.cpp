```cpp
vector<int> l3;
for(int i=0;i<l1.size();i++)
    for(int j=0;j<l2.size();j++)
        if(l1[i]==l2[j]) l3.push_back(l1[i]);
sort(l3.begin(),l3.end());
l3.erase(unique(l3.begin(),l3.end()), l3.end());
return l3;
```

