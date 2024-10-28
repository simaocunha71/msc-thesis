    int sum = 0;
    for(int i=1; i<lst.size(); i+=2){
        if(lst[i]%2 == 0){
            sum += lst[i];
        }
    }
    return sum;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}

The function add() calculates the sum of all the even numbers at the odd indices of a given vector. The for loop starts at index 1 and increments by 2 each time, so it only checks odd indices. Inside the loop, it checks if the element at the current odd index is even by using the modulus operator. If it is, it adds it to the sum. Finally, it returns the sum.
*/

/*
