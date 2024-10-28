    vector<int> l_prime;
    for (int i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
            vector<int> temp;
            for (int j=i;j<l.size();j++)
            {
                if (j%3==0)
                {
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(),temp.end());
            l_prime.push_back(temp[0]);
            i+=2;
        }
        else
        {
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
}
} // namespace std; // Not needed
#endif // main_h // Not needed
} // namespace std; // Not needed
#endif // main_h // Not needed
} // namespace std; // Not needed
#endif // main_h // Not needed

