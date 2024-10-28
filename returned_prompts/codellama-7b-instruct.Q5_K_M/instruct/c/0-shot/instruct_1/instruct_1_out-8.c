
    This is a very simple problem, and you can be sure you
    have the right answer if you understand the basics of
    hash functions. If you're not sure about hash functions,
    you should look them up in your favorite search engine.

    The hash function is a one way function, meaning that you
    can't get back the original input from the hash value.
    The hash function is deterministic, meaning that given the
    same input, the hash value will always be the same.

    The output buffer should be allocated by the function,
    and will be returned as a pointer to the start of the
    buffer. The buffer should be freed by the caller when
    it is no longer needed.

    The function should be able to handle inputs of varying
    lengths, and should return a fixed length hash value.

    Here is some example code that demonstrates how to use
    the function:

    int main(void)
    {
        unsigned char *hash;
        unsigned char *input;
        int i;

        input = malloc(100);
        for (i = 0; i < 100; i++)
        {
            input[i] = i;
        }
        hash = hash_function(input, 100, MD5);
        for (i = 0; i < 16; i++)
        {
            printf("%02x", hash[i]);
        }
        printf("\n");
        free(input);
        free(hash);
        return 0;
    }

    int hash_function(unsigned char *input, int length, int algorithm)
    {
        int i;
        unsigned char *hash;

        if (algorithm == MD2)
        {
            hash = MD2_hash(input, length);
        }
        else if (algorithm == MD4)
        {
            hash = MD4_hash(input, length);
        }
        else if (algorithm == MD5)
        {
            hash = MD5_hash(input, length);
        }
        else if (algorithm == SHA)
        {
            hash = SHA_hash(input, length);
        }
