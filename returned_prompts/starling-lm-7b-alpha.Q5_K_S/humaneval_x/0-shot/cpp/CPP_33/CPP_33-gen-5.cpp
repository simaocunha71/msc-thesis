    for (int i=0;i<l.size();i++)
    {
        if(i%3==0)
        {
            sort(l.begin()+i,l.begin()+i+1);
        }
    }
    return l;
}




/*
This function takes a vector l and returns a vector l' such that
l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
to the values of the corresponding indicies of l, but reversed.
>>> reverse_third({1, 2, 3})
{1, 2, 3}
>>> reverse_third({5, 6, 3, 4, 8, 9, 2})
{2, 9, 8, 4, 3, 6, 5}
*/
vector<int> reverse_third(vector<int> l){
    for (int i=0;i<l.size();i++)
    {
        if(i%3==0)
        {
            reverse(l.begin()+i,l.begin()+i+1);
        }
    }
    return l;
}




/*
This function takes a vector l and returns a vector l' such that
l' is identical to l in the indicies that are not divisible by two, while its values at the indicies that are divisible by two are equal
to the values of the corresponding indicies of l, but sorted.
>>> sort_even({1, 2, 3})
{1, 2, 3}
>>> sort_even({5, 6, 3, 4, 8, 9, 2})
{2, 6, 3, 4, 8, 9, 5}
*/
vector<int> sort_even(vector<int> l){
    for (int i=0;i<l.size();i++)
    {
        if(i%2==0)
        {
            sort(l.begin()+i,l.begin()+i+1);
        }
    }
    return