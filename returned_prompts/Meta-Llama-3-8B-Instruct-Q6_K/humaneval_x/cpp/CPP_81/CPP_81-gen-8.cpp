    vector<string> letter_grades;
    for(float grade : grades){
        if(grade > 4.0) grade = 4.0;
        if(grade > 3.7) grade = 3.7;
        if(grade > 3.3) grade = 3.3;
        if(grade > 3.0) grade = 3.0;
        if(grade > 2.7) grade = 2.7;
        if(grade > 2.3) grade = 2.3;
        if(grade > 2.0) grade = 2.0;
        if(grade > 1.7) grade = 1.7;
        if(grade > 1.3) grade = 1.3;
        if(grade > 1.0) grade = 1.0;
        if(grade > 0.7) grade = 0.7;
        if(grade > 0.0) grade = 0.0;

        if(grade >= 4.0) letter_grades.push_back("A+");
        else if(grade >= 3.7) letter_grades.push_back("A");
        else if(grade >= 3.3) letter_grades.push_back("A-");
        else if(grade >= 3.0) letter_grades.push_back("B+");
        else if(grade >= 2.7) letter_grades.push_back("B");
        else if(grade >= 2.3) letter_grades.push_back("B-");
        else if(grade >= 2.0) letter_grades.push_back("C+");
        else if(grade >= 1.7) letter_grades.push_back("C");
        else if(grade >= 1.3) letter_grades.push_back("C-");
        else if(grade >= 1.0) letter_grades.push_back("D+");
        else if(grade >= 0.7) letter_grades.push_back("D");
        else letter_grades.push_back("E");

    }
    return letter_grades;
}

int main()
{
    vector<float> grades = {4.0, 3.5, 1.7, 2.0, 3.2};
    vector<string> letter_grades = numerical_letter_grade(grades);
    for(string letter_grade : letter_grades){
        printf("%s