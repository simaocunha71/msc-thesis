    int count = 0;
    for(int i=0;i<str.length();i++){
        int j=i;
        while(j<str.length() && str[j]==substring[0]){
            bool match = true;
            for(int k=0;k<substring.length();k++){
                if(str[j+k]!=substring[k]){
                    match = false;
                    break;
                }
            }
            if(match){
                count++;
            }
            j++;
        }
    }
    return count;
}



/*
Given an array of integers, find the maximum value in the array, and the index of the maximum value.

>>> max_value_and_index({1,2,3,4,5})
(5, 4)

>>> max_value_and_index({-1,0,1,2,3})
(1, 3)

>>> max_value_and_index({-1,-2,-3,-4,-5})
(-1, 0)


*/

#include<vector>

pair<int,int> max_value_and_index(vector<int> arr){
    int max_val = arr[0];
    int max_index = 0;
    for(int i=1;i<arr.size();i++){
        if(arr[i]>max_val){
            max_val = arr[i];
            max_index = i;
        }
    }
    return make_pair(max_val, max_index);
}


/*
Given an array of integers, find all the prime numbers in the array, and return the indexes of the prime numbers in the array.

>>> prime_indexes({2,3,4,5,6,7,8,9,10,11,12,13,14,15})
(2, 3, 5, 7, 11, 13)

>>> prime_indexes({2,3,4,5,6,7,8,9,10,11,