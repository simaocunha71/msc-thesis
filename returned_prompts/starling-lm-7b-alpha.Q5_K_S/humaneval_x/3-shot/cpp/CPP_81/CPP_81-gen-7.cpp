    vector<string> all_grades;
    int i,j;
    for (i=0;i<grades.size();i++)
    {
        if (grades[i]>=4.0)
        all_grades.push_back("A+");
        else if (grades[i]>=3.7)
        all_grades.push_back("A");
        else if (grades[i]>=3.3)
        all_grades.push_back("A-");
        else if (grades[i]>=3.0)
        all_grades.push_back("B+");
        else if (grades[i]>=2.7)
        all_grades.push_back("B");
        else if (grades[i]>=2.3)
        all_grades.push_back("B-");
        else if (grades[i]>=2.0)
        all_grades.push_back("C+");
        else if (grades[i]>=1.7)
        all_grades.push_back("C");
        else if (grades[i]>=1.3)
        all_grades.push_back("C-");
        else if (grades[i]>=1.0)
        all_grades.push_back("D+");
        else if (grades[i]>=0.7)
        all_grades.push_back("D");
        else if (grades[i]>=0.0)
        all_grades.push_back("D-");
        else
        all_grades.push_back("E");
    }
    return all_grades;
}



