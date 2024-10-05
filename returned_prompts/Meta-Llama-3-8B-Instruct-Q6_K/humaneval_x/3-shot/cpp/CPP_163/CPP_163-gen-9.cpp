    vector<int> result;
    int min_val = (a < b) ? a : b;
    int max_val = (a < b) ? b : a;
    for(int i=min_val; i<=max_val; i++){
        if(i % 2 == 0){
            result.push_back(i);
        }
    }
    return result;
}  // This function is not checking if the input values are positive. It should be checked. 
