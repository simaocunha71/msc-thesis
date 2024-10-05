    int max_prime=2;
    for (int i=2;i<=sqrt(n);i++)
    {
        while (n%i==0)
        {
            max_prime=i;
            n=n/i;
        }
    }
    return max_prime;
}  // Correct
//int largest_prime_factor(int n){
//    int max_prime=2;
//    for (int i=2;i<=sqrt(n);i++)
//    {
//        if (n%i==0)
//        {
//            max_prime=i;
//            n=n/i;
//        }
//    }
//    return max_prime;
//}  // Incorrect, return first factor, not the largest one.  // Correct
//int largest_prime_factor(int n){
//    int max_prime=1;
//    for (int i=2;i<=sqrt(n);i++)
//    {
//        while (n%i==0)
//        {
//            max_prime=i;
//            n=n/i;
//        }
//    }
//    return max_prime;
//}  // Incorrect, return first factor, not the largest one.
//int largest_prime_factor(int n){
//    int max_prime=n;
//    for (int i=2;i<=sqrt(n);i++)
//    {
//        if (n%i==0)
//        {
//            max_prime=i;
//            n=n/i;
//        }
//    }
//    return max_prime;
//}  // Correct
//int largest_prime_factor(int n){
//    int max_prime=1;
//    for (int i=2;i<=sqrt(n);i++)
//    {
//        while (n%i==0)
//        {
//            max_prime=i;
//            n=n/i;
//        }
//    }
//    return max_prime;
//}  // Incorrect, return first factor, not the largest one.  // Correct
int largest_prime_factor(int n){
    int max_prime=2;
    for (int i=2;i*i<=n;i++)
    {
        while (n%i==0)
        {
            max_prime=i;
            n=n/i;
        }
    }
    if (n>1)
        max_prime=n;
    return max_prime;
}  // Correct
//int largest_prime_factor(int n){
//    int max_prime=1;
//    for (int i=2;i<=sqrt(n);i++)
//    {
//        while (n%i==0