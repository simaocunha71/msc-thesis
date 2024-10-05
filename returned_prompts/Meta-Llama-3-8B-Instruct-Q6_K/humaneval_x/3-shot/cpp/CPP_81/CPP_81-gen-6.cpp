    vector<string> grades_letters;
    string grade_letters[8]={"A+", "A", "A-", "B+", "B", "B-", "C+", "C"};
    for (int i=0;i<grades.size();i++)
    {
        if (grades[i]>=4.0)
        grades_letters.push_back("A+");
        else if (grades[i]>3.7)
        grades_letters.push_back("A");
        else if (grades[i]>3.3)
        grades_letters.push_back("A-");
        else if (grades[i]>3.0)
        grades_letters.push_back("B+");
        else if (grades[i]>2.7)
        grades_letters.push_back("B");
        else if (grades[i]>2.3)
        grades_letters.push_back("B-");
        else if (grades[i]>2.0)
        grades_letters.push_back("C+");
        else if (grades[i]>1.7)
        grades_letters.push_back("C");
        else if (grades[i]>1.3)
        grades_letters.push_back("C-");
        else if (grades[i]>1.0)
        grades_letters.push_back("D+");
        else if (grades[i]>0.7)
        grades_letters.push_back("D");
        else
        grades_letters.push_back("E");
    }
    return grades_letters;
}
// The grade_equation function is same as above. You can use it as an example.