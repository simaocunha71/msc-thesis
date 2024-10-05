    int j=0;
    for(int i=0;i<lst1.size();i++){
        for(int k=0;k<lst2.size();k++){
            if(lst1[i].size()<lst2[k].size()){
                j++;
            }
        }
    }
    if(j==lst1.size()){
        return lst2;
    }
    else
        return lst1;



