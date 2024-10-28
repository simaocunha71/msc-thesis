    for(int i = 2; i <= a; i++)
    {
        int j = i;
        while(j <= a)
        {
            if (j == a)
            {
                int k = i;
                bool is_prime = true;
                while(k > 1)
                {
                    if (k % 2 == 0)
                    {
                        is_prime = false;
                        break;
                    }
                    k--;
                }
                if (is_prime) return true;
            }
            j += i;
        }
    }
    return false;
}