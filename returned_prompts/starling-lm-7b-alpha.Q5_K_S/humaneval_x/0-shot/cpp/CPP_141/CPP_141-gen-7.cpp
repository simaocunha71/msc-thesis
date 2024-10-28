    int len = file_name.size();
    int count = 0;
    for (int i = 0; i < len; i++)
    {
        if (file_name[i] >= '0' && file_name[i] <= '9')
        {
            count++;
        }
    }
    if (count > 3)
    {
        return "No";
    }
    int index = file_name.find(".");
    if (index == -1 || index == 0)
    {
        return "No";
    }
    string name_before = file_name.substr(0, index);
    if (name_before.size() == 0 || name_before[0] < 'a' || name_before[0] > 'z' || name_before[0] < 'A' || name_before[0] > 'Z')
    {
        return "No";
    }
    string name_after = file_name.substr(index + 1);
    if (name_after.size() != 3 || name_after != "txt" && name_after != "exe" && name_after != "dll")
    {
        return "No";
    }
    return "Yes";
}


int main()
{
    string file_name = "example.txt";
    printf("%s\n", file_name_check(file_name).c_str());
    file_name = "1example.dll";
    printf("%s\n", file_name_check(file_name).c_str());
    file_name = "example1.txt";
    printf("%s\n", file_name_check(file_name).c_str());
    file_name = "example.txt.1";
    printf("%s\n", file_name_check(file_name).c_str());
    file_name = "example.txt.123";
    printf("%s\n", file_name_check(file_name).c_str());
    file_name = ".example.txt";
    printf("%s\n", file_name_check(file_name).c_str