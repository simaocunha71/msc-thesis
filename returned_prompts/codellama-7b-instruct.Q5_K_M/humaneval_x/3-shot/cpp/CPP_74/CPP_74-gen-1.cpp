    int i;
    int j;
    int total_char_lst1=0;
    int total_char_lst2=0;
    string smaller_lst;
    for (i=0;i<lst1.size();i++){
        total_char_lst1+=lst1[i].length();
    }
    for (j=0;j<lst2.size();j++){
        total_char_lst2+=lst2[j].length();
    }
    if (total_char_lst1<total_char_lst2){
        smaller_lst=lst1;
    }
    else{
        smaller_lst=lst2;
    }
    return smaller_lst;
}


