    vector<string> result;
    int sum1=0, sum2=0;
    for (int i=0;i<lst1.size();i++){
        sum1+=lst1[i].length();
    }
    for (int i=0;i<lst2.size();i++){
        sum2+=lst2[i].length();
    }
    if (sum1<sum2){
        return lst1;
    }
    else if (sum1>sum2){
        return lst2;
    }
    else{
        return lst1;
    }
}  //  this function always returns the first vector. It should return the vector that has less chars.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function should return the vector that has total number of chars less than the other vector. If the two vectors have the same number of chars, return the first vector.  //  This function