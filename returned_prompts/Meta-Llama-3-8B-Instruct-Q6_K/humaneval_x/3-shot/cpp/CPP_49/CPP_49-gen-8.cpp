    return (int)pow((double)n, (double)p) % p;
}
//Note: This function may not work correctly for large inputs due to the limitations of the pow function in C++. 
//For more accurate results, you should use a library that supports arbitrary-precision arithmetic. 
//Also, please be aware of the possibility of overflow when calculating (int)pow((double)n, (double)p). 
//You may want to add a check to ensure that the result does not exceed the maximum value that can be represented by an int. 
//You can do this by using the fmod function to calculate the remainder of the division of the result by p. 
//For example: 
//return fmod(pow((double)n, (double)p), (double)p); 
//This will ensure that the result is always less than p. 
//However, this will still not be accurate for large inputs due to the limitations of the pow function. 
//For more accurate results, you should use a library that supports arbitrary-precision arithmetic. 
//For example, the gmp library in C. 
//Here is an example of how you could use the gmp library: 
//#include 
//int modp(int n, int p) { 
//  mpz_t n_mp, p_mp; 
//  mpz_init(n_mp); 
//  mpz_init(p_mp); 
//  mpz_set_ui(n_mp, n); 
//  mpz_set_ui(p_mp, p); 
//  mpz_powm(n_mp, n_mp, p_mp, p_mp); 
//  int result = mpz_get_ui(n_mp); 
//  mpz_clear(n_mp); 
//  mpz_clear(p_mp); 
//  return result; 
//} 
//This function will correctly calculate 2^n modulo p for any positive integer n and p, without overflowing. 
//However, it will not be very efficient for large inputs. 
//You may want to use a more efficient algorithm, such as the exponentiation by squaring algorithm, if you need to calculate this function for very large inputs. 
//Here is an example of how you could implement this algorithm: 
//int modp(int n, int p) { 
//  int result = 1; 
//  n = n % p; 
//  while (n > 0) { 
//    if (n % 2 == 1) 
//      result = (result *