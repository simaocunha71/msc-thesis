    string temp=b;
    for (int i=0;i<b.length();i++)
    {
        if (a.find(temp)!=string::npos)
        return true;
        temp=temp.substr(1)+temp[0];
    }
    return false;
} //end of function
//test cases
int main()
{
    cout<<cycpattern_check("abcd","abd")<<endl; //false
    cout<<cycpattern_check("hello","ell")<<endl; //true
    cout<<cycpattern_check("whassup","psus")<<endl; //false
    cout<<cycpattern_check("abab","baa")<<endl; //true
    cout<<cycpattern_check("efef","eeff")<<endl; //false
    cout<<cycpattern_check("himenss",'simen')<<endl; //true
    return 0;
}
//end of main function
//end of program

