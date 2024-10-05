    vector<int> l2;
    for(int i = 0; i < l.size(); i++)
    {
        if(i % 3 == 0)
        {
            vector<int> temp;
            for(int j = i; j < l.size(); j++)
            {
                if(j % 3 == 0)
                {
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(), temp.end());
            l2.insert(l2.end(), temp.begin(), temp.end());
            i += (temp.size() - 1);
        }
        else
        {
            l2.push_back(l[i]);
        }
    }
    return l2;
} // This is a simple way to sort the third elements of the vector. It first finds the third elements, then sorts them and inserts them into a new vector. The index is then incremented by the number of elements that were inserted. This way, the correct index is maintained.