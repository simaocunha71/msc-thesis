/*
It is the last week of the semester and the teacher has to give the grades
to students. The teacher has been making her own algorithm for grading.
The only problem is, she has lost the code she used for grading.
She has given you a vector of GPAs for some students and you have to write 
a function that can output a vector of letter grades using the following table:
         GPA       |    Letter grade
          4.0                A+
        > 3.7                A 
        > 3.3                A- 
        > 3.0                B+
        > 2.7                B 
        > 2.3                B-
        > 2.0                C+
        > 1.7                C
        > 1.3                C-
        > 1.0                D+ 
        > 0.7                D 
        > 0.0                D-
          0.0                E


Example:
grade_equation({4.0, 3, 1.7, 2, 3.5}) ==> {"A+", "B", "C-", "C", "A-"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> numerical_letter_grade(vector<float> grades){
	int a=0,b=1,c=2,d,e;
	for (int i = 0; i <grades.size(); i++){
		if(grades[i]>=4.0)a++;
		else if(grades[i]>3){
			if(grades[i]>=b+1 && grades[i]<c-1)d=2;
			else{
				e+=a+b+c+d;
			}
			return {"A"+to_string(a), "B"+to_string(b), "C"+to_string(c)+"-", "D"+to_string(d) + "-", e+"-E"};
		}
		else{
			e