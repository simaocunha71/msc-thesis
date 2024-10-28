    void MD4_hash(unsigned char *message, unsigned int length, unsigned char *output)
    {
        unsigned int i,j;
        unsigned int length_array[2];
        unsigned int state[4];
        unsigned char chunk[64];
        unsigned char temp[16];
        unsigned char *ptr;
        unsigned int x,y,z;
        unsigned int a,b,c,d;
        unsigned int F[16] = {0xd76aa478,0xe8c7b756,0x242070db,0xc1bdceee,0xf57c0faf,0x4787c62a,0xa8304613,0xfd469501,0x698098d8,0x8b44f7af,0xffff5bb1,0x895cd7be,0x6b901122,0xfd987193,0xa679438e,0x49b40821};
        unsigned int G[16] = {0x67452301,0xe3476f2c,0x2c855665,0x70112d1a,0xb5f774f6,0xd0f89791,0x0cc074e8,0x73045739,0x96150564,0xea6578ed,0xf2c34780,0x49b94342,0x5d8aa92b,0x06db68c1,0x34f1050f,0x3f68f534};

        /* set the length of the message */
        length_array[0] = length;
        length_array[1] = length;

        /* copy the state into a buffer */
        state[0] = 0x67452301;
        state[1