    int max_freq=-1;
    int max_num=-1;
    for (int i=1;i<=*max_element(lst.begin(),lst.end());i++){
        int freq=0;
        for (int j=0;j<lst.size();j++){
            if (lst[j]==i){
                freq++;
            }
        }
        if (freq>=i&&freq>max_freq){
            max_freq=freq;
            max_num=i;
        }
    }
    return (max_num>0)?max_num:-1;
}
