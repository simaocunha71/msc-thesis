    bool allEven=true;
    for(int i=0;i<lst1.size();i++){
        if(lst1[i]%2!=0){
            allEven=false;
            break;
        }
    }
    if(allEven){
        return "YES";
    }
    for(int i=0;i<lst2.size();i++){
        if(lst2[i]%2==0){
            for(int j=0;j<lst1.size();j++){
                if(lst1[j]%2!=0){
                    lst1[j]=lst2[i];
                    break;
                }
            }
        }
    }
    bool allEvenAgain=true;
    for(int i=0;i<lst1.size();i++){
        if(lst1[i]%2!=0){
            allEvenAgain=false;
            break;
        }
    }
    if(allEvenAgain){
        return "YES";
    }else{
        return "NO";
    }
}

