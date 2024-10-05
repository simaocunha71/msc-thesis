    for (int i=0;i<a.size();i++)
    {
        string temp=a.substr(i,a.size());
        if (temp.find(b)!=string::npos)
        return true;
    }
    for (int i=0;i<a.size();i++)
    {
        string temp=a.substr(i,a.size());
        for (int j=0;j<a.size();j++)
        {
            temp=temp.substr(j,temp.size());
            if (temp.find(b)!=string::npos)
            return true;
        }
    }
    return false;
}
//or
#include<string>
#include<sstream>
using namespace std;
bool cycpattern_check(string a,string b){
    stringstream s;
    s << a;
    string temp;
    while(getline(s,temp,' '))
    {
        if(temp.find(b)!=string::npos)
        return true;
    }
    return false;
}
//or
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
    string str=a+b;
    size_t found=str.find(b);
    while(found!=string::npos)
    {
        found=str.find(b,found+1);
    }
    return found!=string::npos;
}
//or
#include<string>
#include<sstream>
using namespace std;
bool cycpattern_check(string a,string b){
    string temp;
    for (int i=0;i<a.size();i++)
    {
        for (int j=i;j<a.size();j++)
        {
            temp=a.substr(i,j-i+1);
            if (temp.find(b)!=string::npos)
            return true;
        }
    }
    return false;
}  //using this function we can check if the string b is present in any rotation of string a.  //this function will return true if the string b is present in any rotation of string a.  //it will return false if string b is not present in any rotation of string a.   //we are checking if string b is present in any rotation of string a.   //we are checking this by generating all rotations of string a and then checking if string b is present in any of these rotations.   //if string b is present in any rotation of string a then we will return true.   //if string b is not present in any rotation of string a then we will return false.   //we are using substr function to generate all rotations of string a.   //substr function is used to extract a substring from a given string.   //we are using find