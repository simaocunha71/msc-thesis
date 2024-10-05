    vector<string> letter_grades;
    string Aplus="A+";
    string A="A";
    string Aminus="A-";
    string Bplus="B+";
    string B="B";
    string Bminus="B-";
    string Cplus="C+";
    string C="C";
    string Cminus="C-";
    string Dplus="D+";
    string D="D";
    string Dminus="D-";
    string E="E";
    for (int i=0;i<grades.size();i++)
    {
        if (grades[i]>=4.0)
        letter_grades.push_back(Aplus);
        else if (grades[i]>=3.7)
        letter_grades.push_back(A);
        else if (grades[i]>=3.3)
        letter_grades.push_back(Aminus);
        else if (grades[i]>=3.0)
        letter_grades.push_back(Bplus);
        else if (grades[i]>=2.7)
        letter_grades.push_back(B);
        else if (grades[i]>=2.3)
        letter_grades.push_back(Bminus);
        else if (grades[i]>=2.0)
        letter_grades.push_back(Cplus);
        else if (grades[i]>=1.7)
        letter_grades.push_back(C);
        else if (grades[i]>=1.3)
        letter_grades.push_back(Cminus);
        else if (grades[i]>=1.0)
        letter_grades.push_back(Dplus);
        else if (grades[i]>=0.7)
        letter_grades.push_back(D);
        else if (grades[i]>=0.0)
        letter_grades.push_back(Dminus);
        else
        letter_grades.push_back(E);
    }
    return letter_grades;
}

