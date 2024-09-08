    int max = 0;
    int count = 0;
    for(int i = 0; i < lst.size(); i++){
        int temp = lst[i];
        int tempCount = 0;
        for(int j = 0; j < lst.size(); j++){
            if(lst[j] == temp){
                tempCount++;
            }
        }
        if(temp > 0 && tempCount >= temp){
            if(temp > max){
                max = temp;
            }
        }
    }
    if(max > 0){
        return max;
    }else{
        return -1;
    }
}  



P:
The function `search(vector<int> lst)` is designed to find the greatest integer that is greater than zero, 
and has a frequency greater than or equal to the value of the integer itself. 

The function iterates over each integer in the input vector `lst`. For each integer, it counts the number of times 
it appears in the vector using a temporary count variable `tempCount`. It then checks if the integer is greater 
than zero and if its count is greater than or equal to its value. If both conditions are met, it updates the maximum 
integer `max` if the current integer is greater than `max`.

Finally, the function returns the maximum integer `max` if it is greater than zero, otherwise it returns -1. 

The time complexity of this function is O(n^2) due to the nested loops, where n is the size of the input vector. 
The space complexity is O(1) as it only uses a constant amount of space to store the maximum integer and the temporary 
count variable. 





T:
1. The input vector is not empty.
2. The input vector contains only positive integers.
3. The function should return -1 if no such a value exist.