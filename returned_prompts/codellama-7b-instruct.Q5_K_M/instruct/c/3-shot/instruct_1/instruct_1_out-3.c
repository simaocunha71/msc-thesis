{
  char *hash;
  int len;

  switch(algo)
  {
    case MD2:
      len=16;
      hash=calloc(len,1);
      MD2(in,inlen,hash);
      break;
    case MD4:
      len=16;
      hash=calloc(len,1);
      MD4(in,inlen,hash);
      break;
    case MD5:
      len=16;
      hash=calloc(len,1);
      MD5(in,inlen,hash);
      break;
    case SHA:
      len=20;
      hash=calloc(len,1);
      SHA(in,inlen,hash);
      break;
    default:
      return NULL;
  }
  return hash;
}

