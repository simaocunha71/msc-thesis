if(lst1.size()==lst2.size())
goto A;
if(lst1.size()>lst2.size())
goto B;
if(lst1.size()<lst2.size())
goto C;
return lst1;
B:
if(lst1.size()==lst2.size())
goto B;
if(lst1.size()>lst2.size())
goto C;
if(lst1.size()<lst2.size())
goto A;
C:
if(lst1.size()==lst2.size())
goto C;
if(lst1.size()>lst2.size())
goto A;
if(lst1.size()<lst2.size())
goto B;
}






int main(int argc, char const *argv[]){
vector<string> v1={"hi","admin"};
vector<string> v2={"hI","hi"};
vector<string> v3={"hi","admin"};
vector<string> v4={"hi","admin"};


printf("%s\n",total_match(v1,v2).front().c_str());
printf("%s\n",total_match(v3,v4).front().c_str());


return 0;
}





