  vector<string> result;
  for(int i=0; i<grades.size(); i++){
    if(grades[i] == 4.0)
      result.push_back("A+");
    else if(grades[i] > 3.7)
      result.push_back("A");
    else if(grades[i] > 3.3)
      result.push_back("A-");
    else if(grades[i] > 3.0)
      result.push_back("B+");
    else if(grades[i] > 2.7)
      result.push_back("B");
    else if(grades[i] > 2.3)
      result.push_back("B-");
    else if(grades[i] > 2.0)
      result.push_back("C+");
    else if(grades[i] > 1.7)
      result.push_back("C");
    else if(grades[i] > 1.3)
      result.push_back("C-");
    else if(grades[i] > 1.0)
      result.push_back("D+");
    else if(grades[i] > 0.7)
      result.push_back("D");
    else if(grades[i] > 0.0)
      result.push_back("D-");
    else
      result.push_back("E");
  }
  return result;
}

/*
The function works by iterating through the grades vector and checking each value 
against the conditions given in the problem. When a grade matches a condition, 
the corresponding letter grade is added to the result vector.
*/
B:

#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
    vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
    vector<string> result = numerical_letter_grade(grades);
    for(int i = 0; i < result.size(); i++)
        cout<<result[i]<<" ";
    return 0;
}
