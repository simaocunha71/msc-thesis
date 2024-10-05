    vector<string> output;
    for(int i = 0; i < grades.size(); i++)
    {
        if(grades[i] >= 4.0)
        {
            output.push_back("A+");
            continue;
        }
        if(grades[i] > 3.7)
        {
            output.push_back("A");
            continue;
        }
        if(grades[i] > 3.3)
        {
            output.push_back("A-");
            continue;
        }
        if(grades[i] > 3.0)
        {
            output.push_back("B+");
            continue;
        }
        if(grades[i] > 2.7)
        {
            output.push_back("B");
            continue;
        }
        if(grades[i] > 2.3)
        {
            output.push_back("B-");
            continue;
        }
        if(grades[i] > 2.0)
        {
            output.push_back("C+");
            continue;
        }
        if(grades[i] > 1.7)
        {
            output.push_back("C");
            continue;
        }
        if(grades[i] > 1.3)
        {
            output.push_back("C-");
            continue;
        }
        if(grades[i] > 1.0)
        {
            output.push_back("D+");
            continue;
        }
        if(grades[i] > 0.7)
        {
            output.push_back("D");
            continue;
        }
        if(grades[i] > 0.0)
        {
            output.push_back("D-");
            continue;
        }
        if(grades[i] == 0.0)
        {
            output.push_back("E");
            continue;
        }
    }
    return output;
}

int main()
{
    vector<float> grades = {4.0, 3, 