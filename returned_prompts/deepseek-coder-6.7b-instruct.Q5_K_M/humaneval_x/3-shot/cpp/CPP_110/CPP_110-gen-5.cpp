    int odd_lst1_count = 0;
    int odd_lst2_count = 0;
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i] % 2 != 0){
            odd_lst1_count++;
        }
    }
    for(int i = 0; i < lst2.size(); i++){
        if(lst2[i] % 2 != 0){
            odd_lst2_count++;
        }
    }
    if(odd_lst1_count > odd_lst2_count){
        return "NO";
    }
    else{
        return "YES";
    }
}


