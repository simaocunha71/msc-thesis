    vector<string> all_grades;
    char letter;
    float gpa;
    int i;
    for (i=0;i<grades.size();i++)
    {
        gpa=grades[i];
        if (gpa>4.0)
        gpa=4.0;
        if (gpa>=3.7)
        letter='A';
        if (gpa>=3.3)
        letter='A-';
        if (gpa>=3.0)
        letter='B+';
        if (gpa>=2.7)
        letter='B';
        if (gpa>=2.3)
        letter='B-';
        if (gpa>=2.0)
        letter='C+';
        if (gpa>=1.7)
        letter='C';
        if (gpa>=1.3)
        letter='C-';
        if (gpa>=1.0)
        letter='D+';
        if (gpa>=0.7)
        letter='D';
        if (gpa>=0.0)
        letter='D-';
        if (gpa<0.0)
        letter='E';

        if (letter=='A')
        all_grades.push_back("A+");
        if (letter=='A-')
        all_grades.push_back("A-");
        if (letter=='B+')
        all_grades.push_back("B+");
        if (letter=='B')
        all_grades.push_back("B");
        if (letter=='B-')
        all_grades.push_back("B-");
        if (letter=='C+')
        all_grades.push_back("C+");
        if (letter=='C')
        all_grades.push_back("C");
        if (letter=='C-')
        all_grades.push_back("C-");
        if (letter=='D+')
        all_grades.push_back("D+");
        if (letter=='D')
        all_grades.push_back("D");
        if (