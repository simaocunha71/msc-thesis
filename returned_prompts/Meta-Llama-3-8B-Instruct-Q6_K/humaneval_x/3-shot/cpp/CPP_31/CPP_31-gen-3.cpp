    if (n<2)
    return false;
    for (long long i=2;i*i<=n;i++)
    if (n%i==0)
    return false;
    return true;
}
// Note: This function may not work correctly for very large numbers due to overflow issues. For such
// cases, you may need to use a library function or a more sophisticated algorithm.