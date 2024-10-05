    vector<string> letter_grade;
    char chr;
    int i;
    for (i=0;i<grades.size();i++)
    {
        if (grades[i]>=4.0)
        {
            chr='A';
            letter_grade.push_back(chr+'+');
        }
        if (grades[i]>3.7 && grades[i]<4.0)
        {
            chr='A';
            letter_grade.push_back(chr+' ');
        }
        if (grades[i]>3.3 && grades[i]<=3.7)
        {
            chr='A';
            letter_grade.push_back(chr+'-');
        }
        if (grades[i]>3.0 && grades[i]<=3.3)
        {
            chr='B';
            letter_grade.push_back(chr+'+');
        }
        if (grades[i]>2.7 && grades[i]<=3.0)
        {
            chr='B';
            letter_grade.push_back(chr+' ');
        }
        if (grades[i]>2.3 && grades[i]<=2.7)
        {
            chr='B';
            letter_grade.push_back(chr+'-');
        }
        if (grades[i]>2.0 && grades[i]<=2.3)
        {
            chr='C';
            letter_grade.push_back(chr+'+');
        }
        if (grades[i]>1.7 && grades[i]<=2.0)
        {
            chr='C';
            letter_grade.push_back(chr+' ');
        }
        if (grades[i]>1.3 && grades[i]<=1.7)
        {
            chr='C';
            letter_grade.push_back(chr+'-');
        }
        if (grades[i]>1.0 && grades[i]<=1.3)
        {
            chr='D';
            letter_grade.push_back(chr+'+');
        }
        if (grades[i]>0.7 && grades[i]<=1.0)
        {
            chr='D';
            letter_grade.push_back(chr+' ');
        }
        if (grades[i]>0.0 && grades[i]<=0.7)
        {
            chr='D';
            letter_grade.push_back(chr+'-');
        }
        if (grades[i]==0.0)
        {
            chr='E';
            letter_grade.push_back(chr+' ');
        }
    }
    return letter_grade;
}

