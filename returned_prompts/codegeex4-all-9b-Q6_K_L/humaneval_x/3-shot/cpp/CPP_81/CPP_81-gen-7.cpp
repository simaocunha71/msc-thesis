    vector<string> all_grades;
    float grade;
    int i;
    for (i=0;i<grades.size();i++)
    {
        grade=grades[i];
        if (grade==4.0)
        all_grades.push_back("A+");
        if (grade>3.7)
        all_grades.push_back("A");
        if (grade>3.3)
        all_grades.push_back("A-");
        if (grade>3.0)
        all_grades.push_back("B+");
        if (grade>2.7)
        all_grades.push_back("B");
        if (grade>2.3)
        all_grades.push_back("B-");
        if (grade>2.0)
        all_grades.push_back("C+");
        if (grade>1.7)
        all_grades.push_back("C");
        if (grade>1.3)
        all_grades.push_back("C-");
        if (grade>1.0)
        all_grades.push_back("D+");
        if (grade>0.7)
        all_grades.push_back("D");
        if (grade>0.0)
        all_grades.push_back("D-");
        if (grade==0.0)
        all_grades.push_back("E");
    }
    return all_grades;
}