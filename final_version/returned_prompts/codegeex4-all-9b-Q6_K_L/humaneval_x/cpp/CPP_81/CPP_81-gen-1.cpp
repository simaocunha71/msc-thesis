vector<string> result;
for(int i=0;i<grades.size();i++){
    if(grades[i]==4.0) result.push_back("A+");
    if(grades[i]>3.7) result.push_back("A");
    if(grades[i]>3.3) result.push_back("A-");
    if(grades[i]>3.0) result.push_back("B+");
    if(grades[i]>2.7) result.push_back("B");
    if(grades[i]>2.3) result.push_back("B-");
    if(grades[i]>2.0) result.push_back("C+");
    if(grades[i]>1.7) result.push_back("C");
    if(grades[i]>1.3) result.push_back("C-");
    if(grades[i]>1.0) result.push_back("D+");
    if(grades[i]>0.7) result.push_back("D");
    if(grades[i]>0.0) result.push_back("D-");
    if(grades[i]==0.0) result.push_back("E");
}
return result;
}

B:
vector<string> numerical_letter_grade(vector<float> grades){

    vector<string> result;
    for(int i=0;i<grades.size();i++){
        if(grades[i]>=4.0) result.push_back("A+");
        if(grades[i]>=3.7) result.push_back("A");
        if(grades[i]>=3.3) result.push_back("A-");
        if(grades[i]>=3.0) result.push_back("B+");
        if(grades[i]>=2.7) result.push_back("B");
        if(grades[i]>=2.3) result.push_back("B-");
        if(grades[i]>=2.0) result.push_back("C+");
        if(grades[i]>=1.7) result.push_back("C");
        if(grades[i]>=1.3) result.push_back("C-");
        if(grades[i]>=1.0) result.push_back("D+");
        if(grades[i]>=0.7) result.push_back("D");
        if(grades[i]>=0.0) result.push_back("D-");
        if(grades[i]==0.0) result.push_back("E");
    }
    return result;
}

C:
vector<string> numerical_letter_grade(vector<float> grades){

    vector<string> result;
    for(int i=0;i<