vector<string> v;
for (int i = 0; i < str.size(); i++)
{
    v.push_back(str.substr(0, i + 1));
}
return v;
}
