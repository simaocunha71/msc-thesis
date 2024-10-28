    vector<int> result;
    int even=0;
    int odd=0;
    for (int i=1;i<=n;i++){
        string s=to_string(i);
        if (s==string(s.rbegin(),s.rend())){
            if (i%2==0)
                even++;
            else
                odd++;
        }
    }
    result.push_back(even);
    result.push_back(odd);
    return result;
} // This solution works but it's not efficient for large inputs. We can do this by generating all numbers and checking if they are palindrome, this could be time consuming. We can do this by generating only even and odd numbers and checking if they are palindrome. This will be more efficient. But it's still not optimal. We can use a more mathematical approach to solve this. We can generate all palindrome numbers and then count them. This will be more efficient. But this is still not the optimal solution. We can use a mathematical formula to calculate the number of palindrome numbers directly. This will be the optimal solution. We can use the following formula: The number of even palindrome numbers is the sum of the number of even numbers with one digit and the number of even numbers with two digits, and the number of odd palindrome numbers is the sum of the number of odd numbers with one digit and the number of odd numbers with two digits. This will be the optimal solution. We can use the following code to implement this: ```cpp #include<stdio.h> #include<vector> #include<string> using namespace std; vector<int> even_odd_palindrome(int n) {     vector<int> result;     int even=0;     int odd=0;     for (int i=1;i<=9;i++){         string s=to_string(i);         if (s==string(s.rbegin(),s.rend())){             even++;         }     }     for (int i=10;i<=n;i=i+2){         string s=to_string(i);         if (s==string(s.rbegin(),s.rend())){             even++;         }     }     for (int i=1;i<=9;i=i+2){         string s=to_string(i);         if (s==string(s.rbegin(),s.rend())){             odd++;         }     }     for (int i=11;i<=n;i=i+2){         string s=to_string(i);         if (s==string(s.rbegin(),s