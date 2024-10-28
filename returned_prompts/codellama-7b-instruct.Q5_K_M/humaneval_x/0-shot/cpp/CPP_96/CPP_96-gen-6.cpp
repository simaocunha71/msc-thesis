vector<int>v;
for(int i=2;i<n;i++){
    if(i%2==0||i%3==0||i%5==0){
        continue;
    }
    v.push_back(i);
}
return v;
}

