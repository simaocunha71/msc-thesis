    vector<int> pile(n);
    for(int i=0;i<n;i++){
        pile[i]=i+1;
        if(i%2==0&&n%2==1)
            pile[i]=pile[i]+1;
        if(i%2==1&&n%2==0)
            pile[i]=pile[i]+1;
    }
    return pile;
}


/*
Given a string, find the first position of a substring in the string. Return -1 if the substring is not found.

Examples:
>>> find_substring("Hello, world", "Hello")
0
>>> find_substring("Hello, world", "W")
4
>>> find_substring("Hello, world", "Wo")
-1
*/
#include<string>
int find_substring(string s1,string s2){
B:
    int n1=s1.size();
    int n2=s2.size();
    for(int i=0;i<n1;i++){
        if(s1[i]==s2[0]){
            int j=i+1;
            for(int k=1;k<n2;k++){
                if(s1[j]!=s2[k]){
                    j++;
                }
            }
            if(j==i+n2){
                return i;
            }
        }
    }
    return -1;
}


/*
Given a string, find the first position of a substring in the string. Return -1 if the substring is not found.

Examples:
>>> find_substring("Hello, world", "Hello")
0
>>> find_substring("Hello, world", "W")
4
>>> find_substring("Hello, world", "Wo")
-1
*/
#include<string>
int find_substring(string s1,string s2){
C:
    int n1=s1.size();
    int n2=s2.size();
    for(int i=0;i<n1;i++){
        if(s1[i]==