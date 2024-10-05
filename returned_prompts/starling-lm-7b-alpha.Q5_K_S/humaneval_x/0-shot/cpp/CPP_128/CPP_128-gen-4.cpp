    int res=0,prod=1;
    for(int i=0;i<arr.size();i++)
    {
        if(arr[i]==0)
        {
            res+=0;
        }
        else if(arr[i]>0)
        {
            res+=abs(arr[i]);
            prod*=1;
        }
        else if(arr[i]<0)
        {
            res+=abs(arr[i]);
            prod*=-1;
        }
    }
    if(prod==-1)
    {
        return -res;
    }
    else
    {
        return res;
    }
}




/*
You are given a vector arr of integers and you need to return
sum of magnitudes of integers multiplied by product of all signs
of each number in the vector, represented by 1, -1 or 0.
Note: return -32768 for empty arr.

Example:
>>> prod_signs({1, 2, 2, -4}) == -9
>>> prod_signs({0, 1}) == 0
>>> prod_signs({}) == -32768
*/



/*
You are given two vectors arr1 and arr2 of integers and you need to return
sum of magnitudes of integers multiplied by product of all signs
of each number in the vectors, represented by 1, -1 or 0.
Note: return -32768 for empty arr.

Example:
>>> prod_signs({1, 2, 2, -4}, {3, -5, 0}) == -5
>>> prod_signs({0}, {1}) == 0
>>> prod_signs({}, {}) == -32768

*/
int prod_signs(vector<int> arr1,vector<int> arr2)
{
    int res=0,prod=1;
    for(int i=0;i<arr1.size();i++)
    {
        if(arr1[i]==0)
        {
            res+=0;
        }
        else if(