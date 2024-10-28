    set<int> s;
    for (int i=0;i<l.size();i++)
    {
        int comp = -l[i];
        if (s.find(comp)!=s.end())
            return true;
        s.insert(l[i]);
    }
    return false;
}  // Time complexity: O(n), where n is the size of the input vector. Space complexity: O(n), where n is the size of the input vector.  This is because we are using a set to store unique elements from the vector.  The set operations like insertion and search take constant time on average.