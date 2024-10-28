    string res;
    int cnt = 0;
    for(char c : text){
        if(c == ' '){
            cnt++;
            if(cnt == 1) res += '_';
        } else {
            if(cnt > 1) {res += '-'; cnt = 0;}
            else if(cnt == 1) {res += '_'; cnt = 0;}
            res += c;
        }
    }
    if(cnt > 1) res += '-';
    return res;
}

int main() {
    printf("%s\n", fix_spaces("Example").c_str());
    printf("%s\n", fix_spaces("Example 1").c_str());
    printf("%s\n", fix_spaces(" Example 2").c_str());
    printf("%s\n", fix_spaces(" Example  3").c_str());
    return 0;
}
*/


A: The problem is not in the code you provided, but in the code you didn't provide. You didn't provide a main function to test the function you wrote.
Here is an example of how you can test your function:

#include <iostream>
#include <string>

std::string fix_spaces(std::string text)
{
    std::string res;
    int cnt = 0;

    for (char c : text)
    {
        if (c == ' ')
        {
            cnt++;
            if (cnt == 1)
                res += '_';
        }
        else
        {
            if (cnt > 1)
            {
                res += '-';
                cnt = 0;
            }
            else if (cnt == 1)
            {
                res += '_';
                cnt = 0;
            }
            res += c;
        }
    }

    if (cnt > 1)
        res += '-';

    return res;
}

int main()
{
    std::string test1 = "Example";
    std::string result1 = fix_spaces(test1);
    std::cout <<