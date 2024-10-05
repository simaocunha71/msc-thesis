    vector<string> letter_grades;
    string grade;
    for(int i=0;i<grades.size();i++){
        if(grades[i]==4.0)
            grade="A+";
        else if(grades[i]>3.7)
            grade="A";
        else if(grades[i]>3.3)
            grade="A-";
        else if(grades[i]>3.0)
            grade="B+";
        else if(grades[i]>2.7)
            grade="B";
        else if(grades[i]>2.3)
            grade="B-";
        else if(grades[i]>2.0)
            grade="C+";
        else if(grades[i]>1.7)
            grade="C";
        else if(grades[i]>1.3)
            grade="C-";
        else if(grades[i]>1.0)
            grade="D+";
        else if(grades[i]>0.7)
            grade="D";
        else if(grades[i]>0.0)
            grade="D-";
        else grade="E";
        letter_grades.push_back(grade);
    }
    return letter_grades;
}


