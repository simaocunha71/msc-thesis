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
        }else if(grades[i] >= -0.1){
            result.push_back("E");
        }
    }
    return result;
}

int main(){
    vector<float> grades;
    vector<string> letter_grade;
    string input;
    while(cin >> input){
        if(input == "END")break;
        grades.push_back(stof(input));
    }
    letter_grade = numerical_letter_grade(grades);
    for(int i = 0; i < letter_grade.size(); i++){
        cout << letter_grade[i] << "\n";
    }
    return 0;
}







