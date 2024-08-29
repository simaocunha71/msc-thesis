/*
The function has two loops, one for counting the frequency of each integer and another for finding the greatest integer that meets the condition. 
The function takes a vector of integers as input and returns an integer.
The function works as follows:
1. Create a vector of integers to store the frequency of each integer.
2. Create a variable to store the greatest integer that meets the condition.
3. Loop through the input vector and count the frequency of each integer.
4. Loop through the frequency vector and find the greatest integer that meets the condition.
5. Return the greatest integer that meets the condition or -1 if no such value exists.
*/

int search(vector<int> lst){
    vector<int> freq(lst.size(),0);
    int max=-1;
    for(int i=0;i<lst.size();i++){
        freq[lst[i]]++;
    }
    for(int i=0;i<freq.size();i++){
        if(freq[i]>=i){
            max=i;
        }
    }
    return max;
}