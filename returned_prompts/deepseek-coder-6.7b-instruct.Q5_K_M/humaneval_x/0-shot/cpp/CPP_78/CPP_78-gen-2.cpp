    int count = 0;
    string prime_hex = "2357BDF";
    for (int i = 0; i < num.size(); i++)
    {
        if (prime_hex.find(num[i]) != string::npos)
        {
            count++;
        }
    }
    return count;
}

int main()
{
    printf("%d\n", hex_key("AB"));  // 1
    printf("%d\n", hex_key("1077E")); // 2
    printf("%d\n", hex_key("ABED1A33")); // 4
    printf("%d\n", hex_key("123456789ABCDEF0")); // 6
    printf("%d\n", hex_key("2020")); // 2
}
