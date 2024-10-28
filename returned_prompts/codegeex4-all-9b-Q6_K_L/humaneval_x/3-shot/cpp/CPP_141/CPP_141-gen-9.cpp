    int i;
    int dot=0;
    int num=0;
    for (i=0;i<file_name.length();i++){
        if (file_name[i]=='.')
            dot+=1;
        if (file_name[i]>=48 && file_name[i]<=57)
            num+=1;
    }
    if (dot==1 && num<=3 && (file_name[0]>=65 && file_name[0]<=90) || (file_name[0]>=97 && file_name[0]<=122) && (file_name[file_name.length()-1]=="txt" || file_name[file_name.length()-1]=="exe" || file_name[file_name.length()-1]=="dll"))
        return "Yes";
    else
        return "No";

}