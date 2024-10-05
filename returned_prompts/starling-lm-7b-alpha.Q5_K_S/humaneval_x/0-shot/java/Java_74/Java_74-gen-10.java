    int length1 = lst1.size();
    int length2 = lst2.size();
    if(length1 < length2){
        return lst1;
    }else if(length1 > length2){
        return lst2;
    }else{
        int sum1 = 0;
        int sum2 = 0;
        for(int i = 0; i < length1; i++){
            sum1 += lst1.get(i).length();
        }
        for(int i = 0; i < length2; i++){
            sum2 += lst2.get(i).length();
        }
        if(sum1 < sum2){
            return lst1;
        }else if(sum1 > sum2){
            return lst2;
        }else{
            for(int i = 0; i < length1; i++){
                if(sum1 < sum2){
                    return lst1;
                }else if(sum1 > sum2){
                    return lst2;
                }else{
                    sum1 = 0;
                    sum2 = 0;
                }
            }
        }
        return lst1;
    }
    }
}




















































































































































































































