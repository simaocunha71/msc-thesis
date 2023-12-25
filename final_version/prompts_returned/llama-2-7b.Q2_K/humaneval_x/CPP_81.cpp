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
	int max = 0, min = 125;   //maximum grade and minimum grade according to the table.
   for(auto i=min;i<=max;++i)    //looping through each value in vector of gpa's to get letter grade.
     if (grades[0] >= i && grades[1] < max){
        string temp="A"+to_string(i); 
		return {temp, temp, temp, temp};   //return vector of letter grades.
     }else if(grades[1] == max)    //If the gpa is in the maximum range then return A+.
       return {"A+", "B", "C-", "C" }; 	//return vector of letter grades.
   else if (i > 0){  //if i value