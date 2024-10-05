    vector<string> letter_grades;
    string letter;
    float gpa;
    int i;
    for (i=0;i<grades.size();i++)
    {
    gpa=grades[i];
    if (gpa>=4.0)
    letter="A+";
    else if (gpa>=3.7)
    letter="A";
    else if (gpa>=3.3)
    letter="A-";
    else if (gpa>=3.0)
    letter="B+";
    else if (gpa>=2.7)
    letter="B";
    else if (gpa>=2.3)
    letter="B-";
    else if (gpa>=2.0)
    letter="C+";
    else if (gpa>=1.7)
    letter="C";
    else if (gpa>=1.3)
    letter="C-";
    else if (gpa>=1.0)
    letter="D+";
    else if (gpa>=0.7)
    letter="D";
    else if (gpa>=0.0)
    letter="D-";
    else if (gpa<0.0)
    letter="E";
    letter_grades.push_back(letter);
    }
    return letter_grades;
}


