    vector<int> count(2,0); // [0, 0]
    num = abs(num); 
    while(num > 0){
        int digit = num % 10;
        if(digit % 2 == 0) count[0]++;
        else count[1]++;
        num /= 10;
    }
    return count;
}

int main(){
    int num;
    printf("Enter a number: ");
    scanf("%d",&num);
    vector<int> counts = even_odd_count(num);
    printf("Even: %d, Odd: %d\n",counts[0],counts[1]);
    return 0;
}

This C++ solution firstly initializes a vector with two elements 0, 0. Then it takes the absolute value of the given number to handle negative numbers. Then it goes into a while loop, where it divides the number by 10 and increments the corresponding index of the vector if the digit is even or odd.
*/

