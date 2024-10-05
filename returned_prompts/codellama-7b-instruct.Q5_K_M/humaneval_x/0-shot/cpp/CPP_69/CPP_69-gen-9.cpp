    int res = -1, i, j, cnt = 0;
    for(i = 0; i < lst.size(); i++){
        cnt = 0;
        for(j = 0; j < lst.size(); j++){
            if(lst[i] == lst[j]) cnt++;
        }
        if(cnt >= lst[i] && lst[i] > res){
            res = lst[i];
        }
    }
    return res;
}

