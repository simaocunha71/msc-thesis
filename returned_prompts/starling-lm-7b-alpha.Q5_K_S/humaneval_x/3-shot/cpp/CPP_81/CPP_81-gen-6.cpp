    vector<string> grades_letters;
    vector<float> all_grades;
    int i;
    float gpa;
    string letter;
    for (i=0;i<grades.size();i++)
    {
        gpa=grades[i];
        if (gpa>4.0)
        gpa=4.0;
        if (gpa<0.0)
        gpa=0.0;
        all_grades.push_back(gpa);
    }

    for (i=0;i<all_grades.size();i++)
    {
        gpa=all_grades[i];
        if (gpa>=3.7)
        letter="A";
        if (gpa>=3.3)
        letter="A-";
        if (gpa>=3.0)
        letter="B+";
        if (gpa>=2.7)
        letter="B";
        if (gpa>=2.3)
        letter="B-";
        if (gpa>=2.0)
        letter="C+";
        if (gpa>=1.7)
        letter="C";
        if (gpa>=1.3)
        letter="C-";
        if (gpa>=1.0)
        letter="D+";
        if (gpa>=0.7)
        letter="D";
        if (gpa>=0.0)
        letter="D-";
        if (gpa<0.0)
        letter="E";

        if (gpa!=3.7&&gpa!=3.3&&gpa!=3.0&&gpa!=2.7&&gpa!=2.3&&gpa!=2.0&&gpa!=1.7&&gpa!=1.3&&gpa!=1.0&&gpa!=0.7&&gpa!=0.0)
        letter="???";

        grades_letters.push_back(letter);
    }
    return grades_letters;
}































