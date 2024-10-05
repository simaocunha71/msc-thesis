    int i=0;
    vector<int> result;
    while(i<music_string.length()){
        if(music_string[i]=='o'){
            result.push_back(4);
            i+=1;
        }else if(music_string[i]=='o'&&music_string[i+1]=='|'){
            result.push_back(2);
            i+=2;
        }else if(music_string[i]=='.'&&music_string[i+1]=='|'){
            result.push_back(1);
            i+=2;
        }
    }
    return result;
}






/*
Input to this function is an integer n and string s, representing the number of lines in an integer grid and the contents of each line.
The contents of each line are represented as a sequence of either 'X' or '.'. If a line contains an 'X', it means that the line is completely filled. If a line contains a '.', it means that the line is completely empty.
Your task is to return the number of empty lines in the grid.

For example, if n=3 and s="XX.X.X.", the function should return 2, because there are two lines in the grid that are completely empty.

>>> count_empty_lines(2, "X.|X.")
1

>>> count_empty_lines(3, "X.|X.|X.")
0

>>> count_empty_lines(4, "X.|X.|..|X.")
2

>>> count_empty_lines(5, "X.|X.|..|X.|.")
3
*/
#include<vector>
#include<string>
using namespace std;
int count_empty_lines(int n, string s){
    int i=0;
    int result=0;
    while(i<n){
        int j=0;
        while(j<s.length()){
            if(s[j]=='.'){
                result++;
                break;
            }
            j++;
        }
        i++;
