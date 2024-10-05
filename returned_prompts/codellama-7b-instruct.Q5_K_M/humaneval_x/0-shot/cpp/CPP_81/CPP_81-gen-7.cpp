    vector<string> output;
    for(int i=0; i<grades.size(); i++){
        float current_grade = grades[i];
        if(current_grade >= 4.0){
            output.push_back("A+");
        }
        else if(current_grade >= 3.7){
            output.push_back("A");
        }
        else if(current_grade >= 3.3){
            output.push_back("A-");
        }
        else if(current_grade >= 3.0){
            output.push_back("B+");
        }
        else if(current_grade >= 2.7){
            output.push_back("B");
        }
        else if(current_grade >= 2.3){
            output.push_back("B-");
        }
        else if(current_grade >= 2.0){
            output.push_back("C+");
        }
        else if(current_grade >= 1.7){
            output.push_back("C");
        }
        else if(current_grade >= 1.3){
            output.push_back("C-");
        }
        else if(current_grade >= 1.0){
            output.push_back("D+");
        }
        else if(current_grade >= 0.7){
            output.push_back("D");
        }
        else if(current_grade >= 0.0){
            output.push_back("D-");
        }
        else if(current_grade <= 0.0){
            output.push_back("E");
        }
    }
    return output;
}


int main(){
    vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
    vector<string> output = numerical_letter_grade(grades);
    for(int i=0; i<output.size(); i++){
        printf("%s\n", output[i].c_str());
    }
}

