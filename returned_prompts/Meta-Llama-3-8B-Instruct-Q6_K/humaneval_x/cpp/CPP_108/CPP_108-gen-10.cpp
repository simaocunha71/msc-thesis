    int count=0;
    for(int i=0;i<n.size();i++){
        int sum=0;
        int num=n[i];
        if(num<0){
            num=-num;
        }
        while(num>0){
            sum+=num%10;
            num=num/10;
        }
        if(sum>0){
            count++;
        }
    }
    return count;
}
int main(){
    vector<int> n = {-1, 11, -11, 1, 1, 2};
    printf("count: %d\n",count_nums(n));
    return 0;
}
C:
The code provided is a C++ solution for the problem. The function `count_nums` takes a vector of integers as input and returns the count of numbers having a sum of digits greater than 0.

The function iterates over each number in the input vector. For each number, it calculates the sum of its digits by repeatedly dividing the number by 10 and adding the remainder to the sum. If the number is negative, it first converts it to positive.

The function checks if the sum of digits is greater than 0. If it is, it increments the count. Finally, the function returns the count.

In the `main` function, a vector `n` is created containing the numbers -1, 11, -11, 1, 1, and 2. The `count_nums` function is called with `n` as input, and the result is printed to the console. The expected output is 3, which is the count of numbers having a sum of digits greater than 0 in the input vector.