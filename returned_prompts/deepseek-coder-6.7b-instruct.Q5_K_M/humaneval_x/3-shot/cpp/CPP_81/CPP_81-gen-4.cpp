    vector<string> letter_grades;
    float gpa;
    for(int i=0; i<grades.size(); i++){
        gpa = grades[i];
        if(gpa == 4.0)
            letter_grades.push_back("A+");
        else if(gpa > 3.7)
            letter_grades.push_back("A");
        else if(gpa > 3.3)
            letter_grades.push_back("A-");
        else if(gpa > 3.0)
            letter_grades.push_back("B+");
        else if(gpa > 2.7)
            letter_grades.push_back("B");
        else if(gpa > 2.3)
            letter_grades.push_back("B-");
        else if(gpa > 2.0)
            letter_grades.push_back("C+");
        else if(gpa > 1.7)
            letter_grades.push_back("C");
        else if(gpa > 1.3)
            letter_grades.push_back("C-");
        else if(gpa > 1.0)
            letter_grades.push_back("D+");
        else if(gpa > 0.7)
            letter_grades.push_back("D");
        else if(gpa > 0.0)
            letter_grades.push_back("D-");
        else
            letter_grades.push_back("E");
    }
    return letter_grades;
}


