    vector<string> letter_grades;
    for  (float grade : grades)
    {
        if  (grade == 4.0)
            letter_grades.push_back("A+");
        else if (grade >= 3.7)
            letter_grades.push_back("A");
        else if (grade >= 3.3)
            letter_grades.push_back("A-");
        else if (grade >= 3.0)
            letter_grades.push_back("B+");
        else if (grade >= 2.7)
            letter_grades.push_back("B");
        else if (grade >= 2.3)
            letter_grades.push_back("B-");
        else if (grade >= 2