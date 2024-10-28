    vector<string> letter_grades;
    string letter_grade;
    for (int i=0;i<grades.size();i++)
    {
        if (grades[i]>=4.0)
        letter_grade="A+";
        if (grades[i]>3.7 && grades[i]<4.0)
        letter_grade="A";
        if (grades[i]>3.3 && grades[i]<3.7)
        letter_grade="A-";
        if (grades[i]>2.7 && grades[i]<3.3)
        letter_grade="B+";
        if (grades[i]>2.3 && grades[i]<2.7)
        letter_grade="B";
        if (grades[i]>2.0 && grades[i]<2.3)
        letter_grade="B-";
        if (grades[i]>1.7 && grades[i]<2.0)
        letter_grade="C+";
        if (grades[i]>1.3 && grades[i]<1.7)
        letter_grade="C";
        if (grades[i]>1.0 && grades[i]<1.3)
        letter_grade="C-";
        if (grades[i]>0.7 && grades[i]<1.0)
        letter_grade="D+";
        if (grades[i]>0.0 && grades[i]<0.7)
        letter_grade="D";
        if (grades[i]<0.0)
        letter_grade="D-";
        letter_grades.push_back(letter_grade);
    }
    return letter_grades;
}


