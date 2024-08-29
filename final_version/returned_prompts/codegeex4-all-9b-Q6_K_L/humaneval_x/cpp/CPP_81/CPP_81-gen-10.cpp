#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
vector<string> numerical_letter_grade(vector<float> grades){
  vector<string> output;
  for(int i=0;i<grades.size();i++){
    if(grades[i]==4.0){
      output.push_back("A+");
    }
    else if(grades[i]>3.7){
      output.push_back("A");
    }
    else if(grades[i]>3.3){
      output.push_back("A-");
    }
    else if(grades[i]>3.0){
      output.push_back("B+");
    }
    else if(grades[i]>2.7){
      output.push_back("B");
    }
    else if(grades[i]>2.3){
      output.push_back("B-");
    }
    else if(grades[i]>2.0){
      output.push_back("C+");
    }
    else if(grades[i]>1.7){
      output.push_back("C");
    }
    else if(grades[i]>1.3){
      output.push_back("C-");
    }
    else if(grades[i]>1.0){
      output.push_back("D+");
    }
    else if(grades[i]>0.7){
      output.push_back("D");
    }
    else if(grades[i]>0.0){
      output.push_back("D-");
    }
    else if(grades[i]==0.0){
      output.push_back("E");
    }
  }
  return output;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
vector<string> numerical_letter_grade(vector<float> grades){
  vector<string> output;
  for(int i=0;i<grades.size();i++){
    if(grades[i]==4.0){
      output.push_back("A+");
    }
    else if(grades[i]>3.7){
      output.push_back("A");
    }
    else if(grades[i]>3.3){
      output.push_back("A-");
    }
    else if(grades[i]>3.0){
      output.push_back("B+");
    }
    else if(grades[i]>2.7){
      output.push_back("B");
    }
    else if(grades[i]>2.3){
      output.push_back("B-");
    }
    else if(grades[i]>2.0){
      output.push_back("C+");
    }
   