    vector<int> common_elements;
    vector<int> l1_sorted=l1;
    vector<int> l2_sorted=l2;
    sort(l1_sorted.begin(),l1_sorted.end());
    sort(l2_sorted.begin(),l2_sorted.end());

    int i=0;
    int j=0;
    while (i<l1_sorted.size() && j<l2_sorted.size()){
        if (l1_sorted[i]==l2_sorted[j]){
            if (!binary_search(common_elements.begin(),common_elements.end(),l1_sorted[i]))
            common_elements.push_back(l1_sorted[i]);
            i+=1;
            j+=1;
        }else if (l1_sorted[i]<l2_sorted[j])
        i+=1;
        else
        j+=1;
    }
    return common_elements;
}



