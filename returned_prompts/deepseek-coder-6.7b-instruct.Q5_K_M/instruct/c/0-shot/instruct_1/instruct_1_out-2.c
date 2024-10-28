
    Your solution should be in C.
*/

#include <openssl/md5.h>
#include <openssl/sha.h>
#include <string.h>

unsigned char* hash_function(unsigned char *input, int length, const EVP_MD *type)
{
    unsigned char *output = (unsigned char*)malloc(EVP_MD_size(type));
    EVP_MD_CTX *context = EVP_MD_CTX_new();
    EVP_DigestInit_ex(context, type, NULL);
    EVP_DigestUpdate(context, input, length);
    EVP_DigestFinal_ex(context, output, NULL);
    EVP_MD_CTX_free(context);
    return output;
}

//test.c
#include <stdio.h>
#include <stdlib.h>
#include "hash_function.c"

int main()
{
    unsigned char *input = (unsigned char*)"Hello, World!";
    int length = strlen((char*)input);

    unsigned char *md5_hash = hash_function(input, length, EVP_md5());
    unsigned char *sha_hash = hash_function(input, length, EVP_sha1());

    for(int i = 0; i < EVP_MD_size(EVP_md5()); i++)
        printf("%02x", md5_hash[i]);
    printf("\n");

    for(int i = 0; i < EVP_MD_size(EVP_sha1()); i++)
        printf("%02x", sha_hash[i]);
    printf("\n");

    free(md5_hash);
    free(sha_hash);

    return 0;
}//include/dataloader/DataLoader.h
#pragma once

#include <vector>
#include <string>

namespace cv
{
    class Mat;
}

namespace dataloader
{
    class DataLoader
    {
    public:
        virtual ~DataLoader() = default;
        virtual std::vector<cv::