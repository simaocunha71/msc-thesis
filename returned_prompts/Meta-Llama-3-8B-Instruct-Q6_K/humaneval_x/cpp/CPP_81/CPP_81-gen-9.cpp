    vector<string> result;
    for(float grade : grades){
        if(grade >= 4.0) result.push_back("A+");
        else if(grade > 3.7) result.push_back("A");
        else if(grade > 3.3) result.push_back("A-");
        else if(grade > 3.0) result.push_back("B+");
        else if(grade > 2.7) result.push_back("B");
        else if(grade > 2.3) result.push_back("B-");
        else if(grade > 2.0) result.push_back("C+");
        else if(grade > 1.7) result.push_back("C");
        else if(grade > 1.3) result.push_back("C-");
        else if(grade > 1.0) result.push_back("D+");
        else if(grade > 0.7) result.push_back("D");
        else result.push_back("E");
    }
    return result;
}

int main(){
    vector<float> grades = {4.0, 3.0, 1.7, 2.0, 3.5};
    vector<string> result = numerical_letter_grade(grades);
    for(string grade : result) printf("%s\n", grade.c_str());
    return 0;
}

C:
```


Solution:
Here is the solution to the problem.

```c
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> numerical_letter_grade(vector<float> grades) {
    vector<string> result;
    for (float grade : grades) {
        if (grade >= 4.0) result.push_back("A+");
        else if (grade > 3.7) result.push_back("A");
        else if (grade > 3.3) result.push_back("A-");
        else if (grade > 3.0) result.push_back("B+");
        else if (grade > 2.7) result.push_back("B");
        else if (grade > 2.3) result.push_back("B-");
        else if (grade > 2.0) result.push_back("C+");
        else if (grade > 1.7) result.push_back("C");
        else if (grade > 1.3) result.push_back("C-");
        else if (grade > 1.0) result