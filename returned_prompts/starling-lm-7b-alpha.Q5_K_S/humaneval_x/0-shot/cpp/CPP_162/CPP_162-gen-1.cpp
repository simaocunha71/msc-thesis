To solve this problem, you can use the OpenSSL library to calculate the MD5 hash of a given string. Here's a step-by-step guide:

1. Include the necessary header files: `<stdio.h>`, `<string>`, and `<openssl/md5.h>`.
2. Define the `string_to_md5` function that takes a `string` parameter named `text`.
3. Check if the `text` string is empty. If it is, return the string "None".
4. Initialize an MD5 context using `MD