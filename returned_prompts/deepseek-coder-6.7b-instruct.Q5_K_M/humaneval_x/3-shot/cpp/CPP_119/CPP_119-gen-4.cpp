    int level=0;
    int i,j;
    for(i=0;i<2;i++){
        for(j=0;j<lst[i].size();j++){
            if(lst[i][j]=='(')
                level+=1;
            if(lst[i][j]==')')
                level-=1;
            if(level<0)
                return "No";
        }
    }
    return (level==0)?"Yes":"No";
}



