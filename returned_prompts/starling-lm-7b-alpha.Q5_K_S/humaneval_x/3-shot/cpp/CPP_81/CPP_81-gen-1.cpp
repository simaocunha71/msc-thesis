    vector<string> all_grades;
    string current_grade;
    int i;
    for (i=0;i<grades.size();i++)
    {
        if (grades[i]>4.0){
            current_grade="A+";
        }
        else if (grades[i]>3.7){
            current_grade="A";
        }
        else if (grades[i]>3.3){
            current_grade="A-";
        }
        else if (grades[i]>3.0){
            current_grade="B+";
        }
        else if (grades[i]>2.7){
            current_grade="B";
        }
        else if (grades[i]>2.3){
            current_grade="B-";
        }
        else if (grades[i]>2.0){
            current_grade="C+";
        }
        else if (grades[i]>1.7){
            current_grade="C";
        }
        else if (grades[i]>1.3){
            current_grade="C-";
        }
        else if (grades[i]>1.0){
            current_grade="D+";
        }
        else if (grades[i]>0.7){
            current_grade="D";
        }
        else if (grades[i]>0.0){
            current_grade="D-";
        }
        else{
            current_grade="E";
        }
        all_grades.push_back(current_grade);
    }
    return all_grades;
}



