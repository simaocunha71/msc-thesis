    if (n<=1)
        return 0;
    else if(n==2)
        return 2;
    else if(n==3)
        return 0;
    else
    {
        int a=0, b=0, c=2, d=0, e;
        for(int i=4; i<=n; i++)
        {
            e = a + b + c + d;
            a = b;
            b = c;
            c = d;
            d = e;
        }
        return e;
    }
}

I've used a simple iterative solution here because the recursive solution would result in an exponential time complexity.
*/

I hope this helps you understand how to approach these problems.

A: Here is a solution using C++ and the STL.

