    vector<string> all_grades;
    int i;
    for (i=0;i<grades.size();i++)
    {
        if (grades[i]>4.0)
        grades[i]=4.0;
        if (grades[i]>3.7)
        all_grades.push_back("A+");
        if (grades[i]>3.3)
        all_grades.push_back("A");
        if (grades[i]>3.0)
        all_grades.push_back("A-");
        if (grades[i]>2.7)
        all_grades.push_back("B+");
        if (grades[i]>2.3)
        all_grades.push_back("B");
        if (grades[i]>2.0)
        all_grades.push_back("B-");
        if (grades[i]>1.7)
        all_grades.push_back("C+");
        if (grades[i]>1.3)
        all_grades.push_back("C");
        if (grades[i]>1.0)
        all_grades.push_back("C-");
        if (grades[i]>0.7)
        all_grades.push_back("D+");
        if (grades[i]>0.0)
        all_grades.push_back("D");
        if (grades[i]>-0.7)
        all_grades.push_back("D-");
        if (grades[i]>-1.0)
        all_grades.push_back("E");
        if (grades[i]<-1.0)
        all_grades.push_back("E");
    }
    return all_grades;
}



