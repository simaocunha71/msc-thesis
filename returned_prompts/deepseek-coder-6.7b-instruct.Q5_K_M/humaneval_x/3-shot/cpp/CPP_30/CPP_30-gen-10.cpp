    vector<float> positive_nums;
    for (int i = 0; i < l.size(); i++){
        if (l[i] > 0){
            positive_nums.push_back(l[i]);
        }
    }
    return positive_nums;
}


