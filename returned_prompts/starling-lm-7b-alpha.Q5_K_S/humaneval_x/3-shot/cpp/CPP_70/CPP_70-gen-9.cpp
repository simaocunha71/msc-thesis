    vector<int> result;
    vector<int>::iterator it=lst.end();
    while (it!=lst.begin()){
        result.push_back(*std::max_element(lst.begin(),it));
        it--;
    }
    result.push_back(*std::min_element(lst.begin(),it));
    return result;
}




