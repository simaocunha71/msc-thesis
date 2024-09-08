    int max = 0;
    for(int i = 0; i < lst.size(); i++){
        int count = 0;
        for(int j = 0; j < lst.size(); j++){
            if(lst[i] == lst[j]){
                count++;
            }
        }
        if(count >= lst[i] && lst[i] > 0 && lst[i] > max){
            max = lst[i];
        }
    }
    if(max > 0){
        return max;
    }
    else{
        return -1;
    }
}

int main(){
    vector<int> lst = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    printf("%d\n", search(lst));
    return 0;
}

Output:
3

Explanation:
The code defines a function `search` that takes a vector of integers as input. The function iterates through the vector and for each integer, it counts its frequency in the vector. If the frequency of the integer is greater than or equal to the integer itself, and the integer is greater than 0, it updates the maximum value. Finally, it returns the maximum value if it is greater than 0, otherwise it returns -1.

In the `main` function, a vector of integers is created and passed to the `search` function. The output is 3, which is the greatest integer that is greater than 0 and has a frequency greater than or equal to the value of the integer itself.