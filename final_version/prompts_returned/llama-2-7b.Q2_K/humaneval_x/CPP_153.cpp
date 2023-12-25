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
	int strenght=0;
	for(size_t i=0;i<extensions.size();++i)
        {
                if ((strngth < extensions[i].length()) && (strength < (extensions[i].length()-class_name.length())) )
                     strenght = extensions[i].length();
	}
      return class_name + "." + extensions[0];
}
int main(void){
	string class="Slices";
	vector<string> exts={"SErviNGSliCes","Cheese","StuFfed"};
	printf("%s\n",Strongest_Extension(class,exts));
   return 0;
}