    vector<int> result;
    vector<int> sorted_lst = lst;
    sort(sorted_lst.begin(), sorted_lst.end());
    for(int i=0; i<sorted_lst.size(); i++){
        if(i % 2 == 0){
            result.push_back(sorted_lst[0]);
            sorted_lst.erase(sorted_lst.begin());
        }else{
            result.push_back(sorted_lst.back());
            sorted_lst.pop_back();
        }
    }
    return result;
}

B:
    vector<int> result;
    vector<int> sorted_lst = lst;
    sort(sorted_lst.begin(), sorted_lst.end());
    for(int i=0; i<sorted_lst.size(); i++){
        if(i % 2 == 0){
            result.push_back(sorted_lst[0]);
            sorted_lst.erase(sorted_lst.begin());
        }else{
            result.push_back(sorted_lst.back());
            sorted_lst.pop_back();
        }
    }
    return result;
}

C:
    vector<int> result;
    vector<int> sorted_lst = lst;
    sort(sorted_lst.begin(), sorted_lst.end());
    for(int i=0; i<sorted_lst.size(); i++){
        if(i % 2 == 0){
            result.push_back(sorted_lst[0]);
            sorted_lst.erase(sorted_lst.begin());
        }else{
            result.push_back(sorted_lst.back());
            sorted_lst.pop_back();
        }
    }
    return result;
}

D:
    vector<int> result;
    vector<int> sorted_lst = lst;
    sort(sorted_lst.begin(), sorted_lst.end());
    for(int i=0; i<sorted_lst.size(); i++){
        if(i % 2 == 0){
            result.push_back(sorted_lst[0]);
            sorted_lst.erase(sorted_lst.begin());
        }else{
            result.push_back(sorted_lst.back());
            sorted_lst.pop_back();
        }
    }
    return result;
}

E:
    vector<int> result;
    vector<int> sorted_lst = lst;
    sort(sorted_lst.begin(), sorted_lst.end());
    for(int i=0; i<sorted_lst.size(); i++){
        if(i % 2 == 0){
            result.push_back(sorted_lst[0]);
            sorted_lst.erase(sorted_lst.begin());
        }else{
            result.push_back(sorted_lst.back());
            sorted_lst.pop_back();
        }
    }
    return result;

Answer: A, B, C, D, E all are correct. They all implement the same algorithm, which is to first sort the list, then iterate over the sorted