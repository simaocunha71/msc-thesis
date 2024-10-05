    long long sum = 0;
    for(int i=0; i<lst.size(); i++){
        if(lst[i] > 0 && lst[i] == (int)lst[i] && lst[i] % 2 != 0)
            sum += pow(lst[i], 2);
    }
    return sum;
}

int main() {
    printf("%lld\n", double_the_difference({1, 3, 2, 0})); // 10
    printf("%lld\n", double_the_difference({-1, -2, 0})); // 0
    printf("%lld\n", double_the_difference({9, -2})); // 81
    printf("%lld\n", double_the_difference({0})); // 0
}
*/

This solution works by iterating through the vector and checking if each number is a positive integer and odd. If it is, we square the number and add it to the sum.
*/

