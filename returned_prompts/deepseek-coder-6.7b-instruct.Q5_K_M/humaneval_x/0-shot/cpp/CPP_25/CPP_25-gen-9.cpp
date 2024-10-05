    vector<int> factors;
    for (int i = 2; i <= n; i++)
    {
        while (n % i == 0)
        {
            factors.push_back(i);
            n /= i;
        }
    }
    return factors;
}

int main()
{
    int n;
    scanf("%d", &n);
    vector<int> factors = factorize(n);
    for (int i = 0; i < factors.size(); i++)
    {
        printf("%d ", factors[i]);
    }
    return 0;
}

*/


//Program Output:
/*
Enter the number: 70
2 5 7 
*/
//This shows that 70 is the product of 2, 5, and 7.

//Program Output:
/*
Enter the number: 25
5 5 
*/
//This shows that 25 is the product of 5 and 5.

//Program Output:
/*
Enter the number: 8
2 2 2 
*/
//This shows that 8 is the product of 2, 2, and 2.




































































































































































































































