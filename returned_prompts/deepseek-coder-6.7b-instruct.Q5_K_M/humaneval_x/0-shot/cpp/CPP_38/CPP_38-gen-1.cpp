string decode_cyclic(string s){ 
    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
    {
        x=s.substr(i*3,3);
        if  (x.length()==3) {
            char last=x[2];
            x=last+x.substr(0,2);
        }
        output=output+x;
    }
    return output;
}


I:
int main()
{
    string s;
    cout<<"Enter a string: ";
    cin>>s;
    string encoded=encode_cyclic(s);
    cout<<"Encoded string: "<<encoded<<endl;
    string decoded=decode_cyclic(encoded);
    cout<<"Decoded string: "<<decoded<<endl;
    return 0;
}


E:
#include<iostream>
using namespace std;

int main()
{
    string s;
    cout<<"Enter a string: ";
    getline(cin,s);
    string encoded=encode_cyclic(s);
    cout<<"Encoded string: "<<encoded<<endl;
    string decoded=decode_cyclic(encoded);
    cout<<"Decoded string: "<<decoded<<endl;
    return 0;
}


D:
#include<iostream>
#include<string>
using namespace std;

int main()
{
    string s;
    cout<<"Enter a string: ";
    getline(cin,s);
    string encoded=encode_cyclic(s);
    cout<<"Encoded string: "<<encoded<<endl;
    string decoded=decode_cyclic(encoded);
    cout<<"Decoded string: "<<decoded<<endl;
    return 0;
}


C:
#include<iostream>
#include<string>
using namespace std;

int main()
