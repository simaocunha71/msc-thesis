    vector<string> all_grades;
    int i;
    string grade;
    for (i=0;i<grades.size();i++)
    {
        if (grades[i]>=4.0){grade="A+";}
        if (grades[i]>3.7){grade="A";}
        if (grades[i]>3.3){grade="A-";}
        if (grades[i]>3.0){grade="B+";}
        if (grades[i]>2.7){grade="B";}
        if (grades[i]>2.3){grade="B-";}
        if (grades[i]>2.0){grade="C+";}
        if (grades[i]>1.7){grade="C";}
        if (grades[i]>1.3){grade="C-";}
        if (grades[i]>1.0){grade="D+";}
        if (grades[i]>0.7){grade="D";}
        if (grades[i]>0.0){grade="D-";}
        if (grades[i]<=0.0){grade="E";}
        all_grades.push_back(grade);
    }
    return all_grades;
}



