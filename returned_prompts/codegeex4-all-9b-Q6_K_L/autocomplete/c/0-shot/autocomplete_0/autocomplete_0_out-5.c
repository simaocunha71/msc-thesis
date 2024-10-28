        MD4_Update(ctx, (unsigned char *)data, data_len);
#else
MD4_Update(ctx, (unsigned char *)data, data_len);
#endif

