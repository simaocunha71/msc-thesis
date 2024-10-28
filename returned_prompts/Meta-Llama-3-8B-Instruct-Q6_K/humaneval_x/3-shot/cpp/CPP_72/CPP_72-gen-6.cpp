    int sum=0;
    string q_str;
    for (int i=0;i<q.size();i++)
    {
        sum+=q[i];
        q_str+=to_string(q[i]);
    }
    if (q_str==string(q_str.rbegin(), q_str.rend()))
    {
        if (sum<=w)
            return true;
        else
            return false;
    }
    else
        return false;
} // this function first calculates the sum of the vector elements and then checks if the string representation of the vector is the same as the reverse of this string. If both conditions are met, the function returns true. Otherwise, it returns false. The second condition checks if the sum of the vector elements is less than or equal to the given weight. If not, the function returns false.