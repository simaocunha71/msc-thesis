    vector<string> result;
    int sum1 = 0, sum2 = 0;
    for(auto str1: lst1){
        sum1 += str1.length();
    }
    for(auto str2: lst2){
        sum2 += str2.length();
    }
    if(sum1 < sum2){
        return lst1;
    }else if(sum1 > sum2){
        return lst2;
    }else{
        return lst1;
    }
}

B:
    vector<string> result;
    int sum1 = 0, sum2 = 0;
    for(auto str1: lst1){
        sum1 += str1.length();
    }
    for(auto str2: lst2){
        sum2 += str2.length();
    }
    if(sum1 < sum2){
        return lst2;
    }else if(sum1 > sum2){
        return lst1;
    }else{
        return lst1;
    }
}

C:
    vector<string> result;
    int sum1 = 0, sum2 = 0;
    for(auto str1: lst1){
        sum1 += str1.length();
    }
    for(auto str2: lst2){
        sum2 += str2.length();
    }
    if(sum1 < sum2){
        return lst2;
    }else if(sum1 > sum2){
        return lst1;
    }else{
        return result;
    }
}

D:
    vector<string> result;
    int sum1 = 0, sum2 = 0;
    for(auto str1: lst1){
        sum1 += str1.length();
    }
    for(auto str2: lst2){
        sum2 += str2.length();
    }
    if(sum1 < sum2){
        return lst1;
    }else if(sum1 > sum2){
        return lst2;
    }else{
        return vector<string>();
    }
}

Correct Answer:
    D:
    vector<string> total_match(vector<string> lst1,vector<string> lst2){
        vector<string> result;
        int sum1 = 0, sum2 = 0;
        for(auto str1: lst1){
            sum1 += str1.length();
        }
        for(auto str2: lst2){
            sum2 += str2.length();
        }
        if(sum1 < sum2){
            return lst1;
        }else if(sum1 > sum2){
            return lst2;
        }else{
            return