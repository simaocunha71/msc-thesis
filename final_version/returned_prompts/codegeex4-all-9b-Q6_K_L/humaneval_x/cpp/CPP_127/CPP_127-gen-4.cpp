/*
#include <cmath>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

string intersection(vector<int> interval1, vector<int> interval2) {
    // Get the start and end of the intersection
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    
    // Calculate the length of the intersection
    int length = end - start;
    
    // Check if the length is a prime number
    if (length < 2) {
        return "NO";
    }
    for (int i = 2; i <= sqrt(length); i++) {
        if (length % i == 0) {
            return "NO";
        }
    }
    
    // If the length is a prime number, return "YES"
    return "YES";
}

int main() {
    vector<int> interval1 = {1, 2};
    vector<int> interval2 = {2, 3};
    cout << intersection(interval1, interval2) << endl; // Output: "NO"
    
    interval1 = {-1, 1};
    interval2 = {0, 4};
    cout << intersection(interval1, interval2) << endl; // Output: "NO"
    
    interval1 = {-3, -1};
    interval2 = {-5, 5};
    cout << intersection(interval1, interval2) << endl; // Output: "YES"
    
    return 0;
}
*/
#include <cmath>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

string intersection(vector<int> interval1, vector<int> interval2) {
    // Get the start and end of the intersection
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    
    // Calculate the length of the intersection
    int length = end - start;
    
    // Check if the length is a prime number
    if (length < 2) {
        return "NO";
    }
    for (int i = 2; i <= sqrt(length); i++) {
        if (length % i == 0) {
            return "NO";
        }
    }
    
    // If the length is a prime number, return "YES"
    return "YES";
}

int main() {
    vector<int> interval1 = {1,