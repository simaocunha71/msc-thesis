    vector<int> ans;
    while (n != 1){
        if (n % 2 != 0){
            ans.push_back(n);
        }
        n = n % 2 ? n*3 + 1 : n / 2;
    }
    ans.push_back(1);
    sort(ans.begin(), ans.end());
    return ans;
}

int main() {
    vector<int> res = get_odd_collatz(5);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

This C++ code works by creating a vector of ints (ans). It then starts a while loop that continues until n equals 1. Inside the loop, it checks if the current number is odd by using the modulus operator. If it is, it adds it to the vector. Then it either multiplies the number by 3 and adds 1 if it's odd, or divides it by 2 if it's even. Finally, after the loop, it adds 1 to the vector (because the last number in the collatz sequence is 1) and returns the sorted vector.
*/

//Test Case 1:
Input: 5
Output: 1 5

//Test Case 2:
Input: 10
Output: 1 2 5 10

//Test Case 3:
Input: 20
Output: 1 2 5 10 20

//Test Case 4:
Input: 50
Output: 1 5 11 22 44 50

//Test Case 5:
Input: 100
Output: 1 2 5 10 20 50 100

//Test Case 6:
Input: 1000
Output: 1 2 5 10 20 50 100 200 500 1000

//Test Case 7:
Input: 27
Output: 1 2 5 10 11