    vector<int> third_elements;
    for(int i=0; i<l.size(); i+=3){
        third_elements.push_back(l[i]);
    }
    sort(third_elements.begin(), third_elements.end());
    for(int i=0, j=0; i<l.size(); i+=3){
        l[i] = third_elements[j++];
    }
    return l;
}


