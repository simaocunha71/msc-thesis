    vector<string> result;
    for(int i = 0; i < grades.size(); i++){
        if(grades[i] >= 4.0){
            result.push_back("A+");
        }else if(grades[i] >= 3.7){
            result.push_back("A");
        }else if(grades[i] >= 3.3){
            result.push_back("A-");
        }else if(grades[i] >= 3.0){
            result.push_back("B+");
        }else if(grades[i] >= 2.7){
            result.push_back("B");
        }else if(grades[i] >= 2.3){
            result.push_back("B-");
        }else if(grades[i] >= 2.0){
            result.push_back("C+");
        }else if(grades[i] >= 1.7){
            result.push_back("C");
        }else if(grades[i] >= 1.3){
            result.push_back("C-");
        }else if(grades[i] >= 1.0){
            result.push_back("D+");
        }else if(grades[i] >= 0.7){
            result.push_back("D");
        }else if(grades[i] >= 0.0){
            result.push_back("D-");
        }else{
            result.push_back("E");
        }
    }
    return result;
}

int main(){
    vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
    for(int i = 0; i < grades.size(); i++){
        printf("%f\t", grades[i]);
    }
    printf("\n");
    vector<string> result = numerical_letter_grade(grades);
    for(int i = 0; i < result.size(); i++){
        printf("%s\t", result[i].c_str());
    }
    printf("\n");
    return 0;
}
