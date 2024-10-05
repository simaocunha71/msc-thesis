    vector<string> final_grade;
    for(int i=0; i<grades.size(); i++){
        if(grades[i]==4.0){
            final_grade.push_back("A+");
        }
        else if(grades[i]>3.7){
            final_grade.push_back("A");
        }
        else if(grades[i]>3.3){
            final_grade.push_back("A-");
        }
        else if(grades[i]>3.0){
            final_grade.push_back("B+");
        }
        else if(grades[i]>2.7){
            final_grade.push_back("B");
        }
        else if(grades[i]>2.3){
            final_grade.push_back("B-");
        }
        else if(grades[i]>2.0){
            final_grade.push_back("C+");
        }
        else if(grades[i]>1.7){
            final_grade.push_back("C");
        }
        else if(grades[i]>1.3){
            final_grade.push_back("C-");
        }
        else if(grades[i]>1.0){
            final_grade.push_back("D+");
        }
        else if(grades[i]>0.7){
            final_grade.push_back("D");
        }
        else if(grades[i]>0.0){
            final_grade.push_back("D-");
        }
        else{
            final_grade.push_back("E");
        }
    }
    return final_grade;
}

int main(){
    vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
    vector<string> final_grades = numerical_letter_grade(grades);
    for(int i=0; i<final_grades.size(); i++){
        printf("%s ", final_grades[i].c_str());
    }
    return 0;
}