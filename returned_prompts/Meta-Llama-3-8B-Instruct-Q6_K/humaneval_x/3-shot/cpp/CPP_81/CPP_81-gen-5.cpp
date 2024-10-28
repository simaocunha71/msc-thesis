    vector<string> letter_grades;
    for(int i=0;i<grades.size();i++){
        float gpa=grades[i];
        if(gpa>4.0) gpa=4.0;
        if(gpa>3.7) letter_grades.push_back("A");
        else if(gpa>3.3) letter_grades.push_back("A-");
        else if(gpa>3.0) letter_grades.push_back("B+");
        else if(gpa>2.7) letter_grades.push_back("B");
        else if(gpa>2.3) letter_grades.push_back("B-");
        else if(gpa>2.0) letter_grades.push_back("C+");
        else if(gpa>1.7) letter_grades.push_back("C");
        else if(gpa>1.3) letter_grades.push_back("C-");
        else if(gpa>1.0) letter_grades.push_back("D+");
        else if(gpa>0.7) letter_grades.push_back("D");
        else letter_grades.push_back("D-");
    }
    return letter_grades;
}  // I used a simple if-else statement to check the GPA and assign the corresponding letter grade. The conditionals are ordered from highest to lowest GPA, so that the correct letter grade is assigned even in case of a tie. The GPA is capped at 4.0 to avoid any potential errors. The letter grades are stored in a vector and returned at the end.