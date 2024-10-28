    vector<string> all_grades;
    string cur_grade;
    float gpa;
    int i;
    for (i=0;i<grades.size();i++)
    {
        gpa=grades[i];
        if (gpa>4.0) gpa=4.0;
        if (gpa>3.7) cur_grade="A";
        if (gpa>3.3) cur_grade="A-";
        if (gpa>3.0) cur_grade="B+";
        if (gpa>2.7) cur_grade="B";
        if (gpa>2.3) cur_grade="B-";
        if (gpa>2.0) cur_grade="C+";
        if (gpa>1.7) cur_grade="C";
        if (gpa>1.3) cur_grade="C-";
        if (gpa>1.0) cur_grade="D+";
        if (gpa>0.7) cur_grade="D";
        if (gpa>0.0) cur_grade="D-";
        if (gpa<=0.0) cur_grade="E";
        all_grades.push_back(cur_grade);
    }
    return all_grades;
}




