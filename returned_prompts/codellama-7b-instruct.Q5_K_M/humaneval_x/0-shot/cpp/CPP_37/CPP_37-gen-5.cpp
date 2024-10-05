    vector<float> temp;
    float odd = l[0];
    for(int i=0;i<l.size();i++){
        if(i%2==0)
            temp.push_back(l[i]);
        else
            odd = l[i];
    }
    temp.push_back(odd);
    sort(temp.begin(),temp.end());
    return temp;
}

