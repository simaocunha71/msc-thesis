    vector<int> pile;
    int i;
    for(i=0;i<n;i++){
        if(i%2==0)
            pile.push_back(i*2);
        else
            pile.push_back(i*2+1);
    }
    return pile;

}






ANSWER:
/*
Here is the step-by-step solution to this problem:

1. Create a vector named 'pile' to store the number of stones in each level of the pile.
2. Use a for loop to iterate over the range from 0 to n (inclusive).
3. Inside the loop, check if the current index 'i' is even or odd using the modulo operator (%).
4. If 'i' is even, add 'i' multiplied by 2 to the 'pile' vector using the 'push_back' function.
5. If 'i' is odd, add 'i' multiplied by 2 plus 1 to the 'pile' vector using the 'push_back' function.
6. Repeat steps 4 and 5 for each index in the range from 0 to n (inclusive).
7. After the loop is finished, return the 'pile' vector.

This solution ensures that the correct number of stones is added to the vector for each level of the pile,
based on whether the current index is even or odd.

The time complexity of this solution is O(n), where n is the input number.
This is because the for loop iterates over the range from 0 to n (inclusive),
and each iteration performs a constant amount of work (adding a number to the vector).

The space complexity of this solution is also O(n), where n is the input number.
This is because the 'pile' vector can have a maximum size of n,
and each element in the vector represents a number in the pile.

Overall, this solution provides an efficient and correct implementation of the problem.

 */




















































