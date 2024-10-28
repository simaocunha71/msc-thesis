    vector<string> all_grades;
    string letter_grade;
    int i;
    for (i=0;i<grades.size();i++)
    {
        if (grades[i]==4.0)
        letter_grade="A+";
        else if (grades[i]>3.7)
        letter_grade="A";
        else if (grades[i]>3.3)
        letter_grade="A-";
        else if (grades[i]>3.0)
        letter_grade="B+";
        else if (grades[i]>2.7)
        letter_grade="B";
        else if (grades[i]>2.3)
        letter_grade="B-";
        else if (grades[i]>2.0)
        letter_grade="C+";
        else if (grades[i]>1.7)
        letter_grade="C";
        else if (grades[i]>1.3)
        letter_grade="C-";
        else if (grades[i]>1.0)
        letter_grade="D+";
        else if (grades[i]>0.7)
        letter_grade="D";
        else if (grades[i]>0.0)
        letter_grade="D-";
        else
        letter_grade="E";
        all_grades.push_back(letter_grade);
    }
    return all_grades;
}

