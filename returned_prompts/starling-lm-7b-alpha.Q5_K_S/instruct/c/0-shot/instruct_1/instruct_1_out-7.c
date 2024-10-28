
    Here's an example of how you can use the function:

```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(void)
    {
        const char *input = "Hello, world!";
        unsigned char *hash;

        hash = md5(input);
        printf("The MD5 hash of '%s' is '%s'\n", input, hash);
        free(hash);

        hash = sha1(input);
        printf("The SHA-1 hash of '%s' is '%s'\n", input, hash);
        free(hash);

        return EXIT_SUCCESS;
    }
```

In this example, the `md5` and `sha1` functions are used to calculate the MD5 and SHA-1 hashes of the input string. The `free` function is used to release the memory allocated by the hash functions.

Here's an implementation of the `md5` function:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

unsigned char *md5(const char *input)
{
    unsigned char *hash;
    MD5_CTX ctx;

    MD5_Init(&ctx);
    MD5_Update(&ctx, (unsigned char *)input, strlen(input));
    MD5_Final(hash, &ctx);

    return hash;
}
```

And here's an implementation of the `sha1` function:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

unsigned char *sha1(const char *input)
{
    unsigned char *hash;
    SHA_CTX ctx;

    SHA1_Init(&ctx);
    SHA1_Update(&ctx, (unsigned char *)input, strlen(input));
    SHA1_Final(hash, &ctx);

    return hash;
}
```

In these implementations, the `