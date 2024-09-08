    vector<string> result;
    for(float i:grades){
        if(i >= 4.0)
            result.push_back("A+");
        else if(i > 3.7)
            result.push_back("A");
        else if(i > 3.3)
            result.push_back("A-");
        else if(i > 3.0)
            result.push_back("B+");
        else if(i > 2.7)
            result.push_back("B");
        else if(i > 2.3)
            result.push_back("B-");
        else if(i > 2.0)
            result.push_back("C+");
        else if(i > 1.7)
            result.push_back("C");
        else if(i > 1.3)
            result.push_back("C-");
        else if(i > 1.0)
            result.push_back("D+");
        else if(i > 0.7)
            result.push_back("D");
        else if(i > 0.0)
            result.push_back("D-");
        else
            result.push_back("E");
    }
    return result;
}

int main(){
    vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
    vector<string> result = numerical_letter_grade(grades);
    for(string i:result)
        printf("%s\n", i.c_str());
    return 0;
}

