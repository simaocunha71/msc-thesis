    string str = s;
    int i = 0;
    string word = "";
    string result = "";

    while (i < str.length())
    {
        if (str[i] != ' ')
        {
            word += str[i];
        }
        else
        {
            sort(word.begin(), word.end());
            result += word;
            result += ' ';
            word = "";
        }
        i++;
    }
    sort(word.begin(), word.end());
    result += word;

    return result;
}

int main()
{
    printf("%s\n", anti_shuffle("Hello World!!!").c_str());
    return 0;
}

*/

/*
