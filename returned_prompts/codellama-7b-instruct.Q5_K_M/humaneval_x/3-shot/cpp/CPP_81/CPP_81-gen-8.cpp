    vector<string> letter_grades;
    for (int i=0;i<grades.size();i++)
    {
        float grade=grades[i];
        if (grade>=4.0)
        letter_grades.push_back("A+");
        if (grade>=3.7)
        letter_grades.push_back("A");
        if (grade>=3.3)
        letter_grades.push_back("A-");
        if (grade>=3.0)
        letter_grades.push_back("B+");
        if (grade>=2.7)
        letter_grades.push_back("B");
        if (grade>=2.3)
        letter_grades.push_back("B-");
        if (grade>=2.0)
        letter_grades.push_back("C+");
        if (grade>=1.7)
        letter_grades.push_back("C");
        if (grade>=1.3)
        letter_grades.push_back("C-");
        if (grade>=1.0)
        letter_grades.push_back("D+");
        if (grade>=0.7)
        letter_grades.push_back("D");
        if (grade<=0.0)
        letter_grades.push_back("E");
    }
    return letter_grades;
}


