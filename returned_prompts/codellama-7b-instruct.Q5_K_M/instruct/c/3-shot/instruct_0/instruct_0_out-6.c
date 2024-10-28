{
  MD4_CTX *ctx;
  uint32_t A,B,C,D;

  ctx = (MD4_CTX *)malloc(sizeof(MD4_CTX));
  ctx->A = 0x67452301;
  ctx->B = 0xefcdab89;
  ctx->C = 0x98badcfe;
  ctx->D = 0x10325476;
  if ( ctx == NULL )
    return NULL;
  MD4_Init(ctx);
  MD4_Update(ctx,message,length);
  MD4_Final(ctx,hash);
  free(ctx);
  return hash;
}
