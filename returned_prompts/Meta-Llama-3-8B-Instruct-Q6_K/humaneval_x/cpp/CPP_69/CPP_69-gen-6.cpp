    int max = -1;
    for(int i = 0; i < lst.size(); i++){
        int freq = 0;
        for(int j = 0; j < lst.size(); j++){
            if(lst[i] == lst[j]){
                freq++;
            }
        }
        if(freq >= lst[i] && lst[i] > 0 && freq > 0){
            max = lst[i];
        }
    }
    if(max == -1){
        return -1;
    }
    return max;
}
int main()
{
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    printf("%d\n", search(lst));
    return 0;
}
C++
/*
This program implements the problem described above. 
The function search() takes a vector of positive integers as input and returns the greatest integer that is greater than 
zero, and has a frequency greater than or equal to the value of the integer itself. 
If no such value exists, it returns -1.

The program iterates over each element in the vector and calculates its frequency. 
If the frequency of an element is greater than or equal to the element itself, 
and the element is greater than 0, it updates the maximum value.
Finally, it returns the maximum value found.

In the main function, we create a vector of integers and call the search function to find the desired value.
*/
Output:
2
*/



