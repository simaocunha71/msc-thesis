    for(auto &grade : grades){
        if(grade <= 0){
            grade = "E";
        }
        else if(grade > 0 && grade < 3.7){
            grade = "A-";
        }
        else if(grade >= 3.7 && grade < 3.3){
            grade = "A";
        }
        else if(grade >= 3.3 && grade < 3.0){
            grade = "A+";
        }
        else if(grade >= 3.0 && grade < 2.7){
            grade = "B-";
        }
        else if(grade >= 2.7 && grade < 2.3){
            grade = "B";
        }
        else if(grade >= 2.3 && grade < 2.0){
            grade = "B+";
        }
        else if(grade >= 2.0 && grade < 1.7){
            grade = "C-";
        }
        else if(grade >= 1.7 && grade < 1.3){
            grade = "C";
        }
        else if(grade >= 1.3 && grade < 1.0){
            grade = "C+";
        }
        else if(grade >= 1.0 && grade < 0.7){
            grade = "D-";
        }
        else if(grade >= 0.7 && grade <= 0.0){
            grade = "D";
        }
    }
    return grades;
}

int main()
{
    vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
    vector<string> output;
    output = numerical_letter_grade(grades);
    for(auto i : output){
        cout << i << endl;
    }
    return 0;
}
