#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> numerical_letter_grade(vector<float> grades) {
        vector<string> results;
        for (const auto& grade : grades) {
            if (grade > 4.0)
                results.push_back("A+");
            else if (grade > 3.7)
                results.push_back("A");
            else if (grade > 3.3)
                results.push_back("A-");
            else if (grade > 3.0)
                results.push_back("B+");
            else if (grade > 2.7)
                results.push_back("B");
            else if (grade > 2.3)
                results.push_back("B-");
            else if (grade > 2.0)
                results.push_back("C+");
            else if (grade > 1.7)
                results.push_back("C");
            else if (grade > 1.3)
                results.push_back("C-");
            else if (grade > 1.0)
                results.push_back("D+");
            else if (grade > 0.7)
                results.push_back("D");
            else if (grade > 0.0)
                results.push_back("D-");
            else
                results.push_back("E");
        }
        return results;
    }
};

int main() {
    Solution solution;
    vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
    vector<string> results = solution.numerical_letter_grade(grades);
    for (const auto& result : results)
        cout << result << " ";
    cout << endl;
    return 0;
}

B:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> numerical_letter_grade(vector<float> grades) {
    vector<string> results;
    for (const auto& grade : grades) {
        if (grade >= 4.0)
            results.push_back("A+");
        else if (grade >= 3.7)
            results.push_back("A");
        else if (grade >= 3.3)
            results.push_back("A-");
        else if (grade >= 3.0)
            results.push_back("B+");
        else if (grade >= 2.7)
            results.push_back("B");
        else if (grade >= 2