    float max=0;
    for(int i=0;i<l.size();i++)
    {
        if(l[i]>max)
        {
            max=l[i];
        }
    }
return max;
}

int main()
{
vector<float> v;
v.push_back(1);
v.push_back(2);
v.push_back(3);
printf("Max element: %f\n",max_element(v));

vector<float> v1;
v1.push_back(5);
v1.push_back(3);
v1.push_back(-5);
v1.push_back(2);
v1.push_back(-3);
v1.push_back(3);
v1.push_back(9);
v1.push_back(0);
v1.push_back(123);
v1.push_back(1);
v1.push_back(-10);
printf("Max element: %f\n",max_element(v1));

return 0;
}
*/

//Code/C++/MaxElement/MaxElement.cpp
#include<iostream>
#include<vector>
using namespace std;

float max_element(vector<float> l){
    float max=0;
    for(int i=0;i<l.size();i++)
    {
        if(l[i]>max)
        {
            max=l[i];
        }
    }
return max;
}

int main()
{
vector<float> v;
v.push_back(1);
v.push_back(2);
v.push_back(3);
cout<<"Max element: "<<max_element(v)<<endl;

vector<float> v1;
v1.push_back(5);
v1.push_back(3);
v1.push_back(-5);
v1.push_back(2);
v1.push_back(-3);
v1.push_back(3);
v1.