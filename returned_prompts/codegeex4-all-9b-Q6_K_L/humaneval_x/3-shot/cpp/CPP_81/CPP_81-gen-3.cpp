    vector<string> all_grades;
    string current_grade;
    float chr;
    int i;
    for (i=0;i<grades.size();i++)
    {
        chr=grades[i];
        if (chr==4.0)
        {
        current_grade="A+";
        }
        if (chr>3.7)
        {
        current_grade="A";
        }
        if (chr>3.3)
        {
            current_grade="A-";
        }
        if (chr>3.0)
        {
            current_grade="B+";
        }
        if (chr>2.7)
        {
            current_grade="B";
        }
        if (chr>2.3)
        {
            current_grade="B-";
        }
        if (chr>2.0)
        {
            current_grade="C+";
        }
        if (chr>1.7)
        {
            current_grade="C";
        }
        if (chr>1.3)
        {
            current_grade="C-";
        }
        if (chr>1.0)
        {
            current_grade="D+";
        }
        if (chr>0.7)
        {
            current_grade="D";
        }
        if (chr>0.0)
        {
            current_grade="D-";
        }
        if (chr==0.0)
        {
            current_grade="E";
        }
        all_grades.push_back(current_grade);
    }
    return all_grades;
}