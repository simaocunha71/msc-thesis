    for(int i = 2; i <= a; i++)
    {
        if (is_prime(i) && is_prime(a/i) && is_prime(a/(i*a/i)))
        {
            return true;
        }
    }
    return false;
}

bool is_prime(int a)
{
    if (a < 2)
    {
        return false;
    }
    for (int i = 2; i * i <= a; i++)
    {
        if (a % i == 0)
        {
            return false;
        }
    }
    return true;
}
}  // namespace std
int main()
{
    cout << is_multiply_prime(30) << endl;
    return 0;
}  // main() function
