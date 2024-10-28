vector<string> grades_letter_grade;
for(int i = 0; i < grades.size(); i++){
    if(grades[i] >= 4.0){
        grades_letter_grade.push_back("A+");
    }else if(grades[i] >= 3.7){
        grades_letter_grade.push_back("A");
    }else if(grades[i] >= 3.3){
        grades_letter_grade.push_back("A-");
    }else if(grades[i] >= 3.0){
        grades_letter_grade.push_back("B+");
    }else if(grades[i] >= 2.7){
        grades_letter_grade.push_back("B");
    }else if(grades[i] >= 2.3){
        grades_letter_grade.push_back("B-");
    }else if(grades[i] >= 2.0){
        grades_letter_grade.push_back("C+");
    }else if(grades[i] >= 1.7){
        grades_letter_grade.push_back("C");
    }else if(grades[i] >= 1.3){
        grades_letter_grade.push_back("C-");
    }else if(grades[i] >= 1.0){
        grades_letter_grade.push_back("D+");
    }else if(grades[i] >= 0.7){
        grades_letter_grade.push_back("D");
    }else if(grades[i] >= 0.0){
        grades_letter_grade.push_back("D-");
    }else{
        grades_letter_grade.push_back("E");
    }
}
return grades_letter_grade;
}

int main(){
    vector<float> grades;
    vector<string> grades_letter;
    grades.push_back(3.7);
    grades.push_back(2.3);
    grades.push_back(1.0);
    grades_letter = numerical_letter_grade(grades);

    for(int i = 0; i