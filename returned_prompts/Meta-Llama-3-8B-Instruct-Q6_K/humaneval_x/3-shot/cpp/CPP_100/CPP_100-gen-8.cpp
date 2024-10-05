    vector<int> pile;
    int stones;
    for (int i=0;i<n;i++)
    {
        if (i%2==0)
        stones=i*2+1;
        else
        stones=i*2+2;
        pile.push_back(stones);
    }
    return pile;
}
// The above function works fine for small inputs, but it would be very inefficient for large inputs.
// You could improve this function by using a more efficient method to generate the sequence of odd and even numbers. 
// For example, you could use the formula for the nth odd or even number: n*2-1 for odd numbers and n*2 for even numbers. 
// This would reduce the time complexity of the function from O(n) to O(1). 
// Here is the improved function:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> make_a_pile(int n){
    vector<int> pile;
    for(int i=1;i<=n;i++){
        pile.push_back(i*2-1+(i%2));
    }
    return pile;
}
// This function first initializes an empty vector to store the result.
// Then it uses a for loop to generate the sequence of odd and even numbers.
// In each iteration of the loop, it calculates the number of stones in the current level using the formula n*2-1+(i%2), where n is the current level and i is the index of the level in the sequence.
// Finally, it returns the resulting vector. 
// This function has a time complexity of O(n) and a space complexity of O(n), where n is the number of levels in the pile. 
// This is because it needs to generate the sequence of odd and even numbers and store it in the vector. 
// The space complexity could be reduced to O(1) if the function does not need to store the sequence of odd and even numbers, but this would require a different approach to solve the problem. 
// For example, the function could return the sum of the sequence of odd and even numbers, instead of storing the sequence in a vector. 
// In this case, the time complexity would still be O(n) and the space complexity would be O(1). 
// However, the function would need to be modified to calculate the sum of the sequence, instead of storing it in a vector. 
// This would require a different approach to solve the problem. 





