    int res = -1;
    int maxFreq = 0;
    for(int i = 0; i < lst.size(); i++){
        int freq = 1;
        for(int j = i+1; j < lst.size(); j++){
            if(lst[i] == lst[j]){
                freq++;
            }
        }
        if(freq >= lst[i] && freq > maxFreq){
            maxFreq = freq;
            res = lst[i];
        }
    }
    return res;
}

// 3 2 2 3 3 3 4 4 4
// 4 1 2 2 3 1

