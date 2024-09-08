    int even = 0;
    int odd = 0;
    while(num != 0){
        int digit = num % 10;
        if(digit % 2 == 0){
            even++;
        }else{
            odd++;
        }
        num /= 10;
    }
    vector<int> result;
    result.push_back(even);
    result.push_back(odd);
    return result;
}
int main(){
    int num = 123;
    vector<int> result = even_odd_count(num);
    cout<<"Even digits: "<<result[0]<<endl;
    cout<<"Odd digits: "<<result[1]<<endl;
    return 0;
}
Output:
Even digits: 1
Odd digits: 2

Explanation:
The function even_odd_count() takes an integer as input and returns a vector where the first element represents the number of even digits and the second element represents the number of odd digits.
The function iterates through each digit of the input integer using a while loop. It checks if the digit is even or odd by using the modulus operator. If the digit is even, it increments the 'even' counter, otherwise it increments the 'odd' counter.
Finally, the function returns a vector containing the counts of even and odd digits.
In the main function, we test the even_odd_count() function with the input 123. The output shows that there is one even digit (3) and two odd digits (1 and 2).

*/



