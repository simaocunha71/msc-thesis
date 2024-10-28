{
  int i,j;
  uint32_t a,b,c,d;
  uint32_t A[4];
  uint32_t B[4];
  uint32_t C[4];
  uint32_t D[4];

  /* Initialize state buffer and hash values */
  A[0]=0x67452301;
  A[1]=0xEFCDAB89;
  A[2]=0x98BADCFE;
  A[3]=0x10325476;

  /* Process message in 64-byte chunks */
  while (msglen>0) {
    /* Copy current chunk to temporary buffer */
    for (i=0;i<64;i++)
      if (i<msglen)
        B[i]=msg[i];
      else
        B[i]=0;

    /* Initialize state buffer */
    B[56]=msglen;
    B[60]=msglen/256;
    B[61]=(msglen/65536)%256;
    B[62]=(msglen/16777216)%256;
    B[63]=(msglen/4294967296)%256;

    /* Process current chunk */
    for (i=0;i<16;i++) {
      A[0]=A[0]+(A[1]&A[2])|(~A[1]&A[3]);
      A[0]=A[0]+(A[0]+B[i]+0x5A827999);
      A[0]=A[0]<<(3)^(A[0]>>(29));
      A[0]=A[0]+A[3];
      A[3]=A[2];
      A[2]=A[1];
      A[1]=A[0];
      A[0]=A[0]+(A[1]&A[2])|(~A[1]&A[3]);
      A[0]=A[0]+(A[0]+B[(i+9)%16]+0x6ED9EBA1);
      A[0]=A[0]<<(7)^(A[0]>>(25));
      A[0]=A[0]+A[3];
      A[3]=A[2];
      A[2]=A[1];
      A[1]=A[0];
      A[0]=A[0]+(A[1]&A[2])|(~A[1]&