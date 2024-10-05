    int count=0;
    vector<int> visited(128,0);

B:
    for(int i=0;i<str.length();i++){
        if(visited[tolower(str[i])]==0 && tolower(str[i]) != ' '){
            visited[tolower(str[i])]=1;
            count++;
        }
    }
    return count;
}
int main(){
    string str;
    printf("Enter the string: ");
    getline(cin,str);
    printf("The number of distinct characters are: %d\n",count_distinct_characters(str));
    return 0;
}
*/

//Test Cases
/*
Test Case 1:
Input: xyzXYZ
Output: 3
Explanation: The distinct characters are x, y, z.

Test Case 2:
Input: Jerry
Output: 4
Explanation: The distinct characters are j, e, r, y.

Test Case 3:
Input: Hello World
Output: 7
Explanation: The distinct characters are h, e, l, o, w, r, d.

Test Case 4:
Input: Programming
Output: 8
Explanation: The distinct characters are p, r, o, g, a, m, i, n.

Test Case 5:
Input: This is a test string
Output: 10
Explanation: The distinct characters are t, h, i, s, a, e, r, n, g, d.
*/

//Test Cases with uppercase and lowercase letters mixed
/*
Test Case 6:
Input: AbcAbc
Output: 3
Explanation: The distinct characters are a, b, c.

Test Case 7:
Input: aBcAbC
Output: 3
Explanation: The distinct characters are a, b, c.

Test Case 8:
Input: ABcABc
Output: 3
Explanation: The distinct characters are a, b, c.

Test Case 9:
Input: abCabC