/*
You will be given the name of a class (a string) and a vector of extensions.
The extensions are to be used to load additional classes to the class. The
strength of the extension is as follows: Let CAP be the number of the uppercase
letters in the extension's name, and let SM be the number of lowercase letters 
in the extension's name, the strength is given by the fraction CAP - SM. 
You should find the strongest extension and return a string in this 
format: ClassName.StrongestExtensionName.
If there are two or more extensions with the same strength, you should
choose the one that comes first in the vector.
For example, if you are given "Slices" as the class and a vector of the
extensions: {"SErviNGSliCes", "Cheese", "StuFfed"} then you should
return "Slices.SErviNGSliCes" since "SErviNGSliCes" is the strongest extension 
(its strength is -1).
Example:
for Strongest_Extension("my_class", {"AA", "Be", "CC"}) == "my_class.AA"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string Strongest_Extension(string class_name,vector<string> extensions){
	int CAP=0,SM=0;
	for(int i = 0;i < class_name.size();i++)
	{
     if((class_name[i] >= 'A' && class_name[i] <= 'Z') || (class_name[i] >= 'a' && class_name[i] <= 'z'))
         CAP++;
     else SM++;
  }

  int index = find(extensions.begin(), extensions.end(), class_name);
  if(index == extensions.size()) return "NULL";
	else
	{
    string strongest_extension;
	for(int i=0;i<extensions[index].size();i++)
     {
         int strength = CAP - SM;
         //cout<<strength <<endl;
         if(strength >