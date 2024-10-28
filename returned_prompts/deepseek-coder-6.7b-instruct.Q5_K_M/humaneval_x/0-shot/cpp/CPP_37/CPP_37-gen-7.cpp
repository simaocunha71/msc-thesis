    vector<float> even_values;
    vector<float> odd_values;
    for(int i=0;i<l.size();i++){
        if(i%2==0){
            even_values.push_back(l[i]);
        }
        else{
            odd_values.push_back(l[i]);
        }
    }
    sort(even_values.begin(),even_values.end());
    for(int i=0;i<even_values.size();i++){
        l[2*i]=even_values[i];
    }
    for(int i=0;i<odd_values.size();i