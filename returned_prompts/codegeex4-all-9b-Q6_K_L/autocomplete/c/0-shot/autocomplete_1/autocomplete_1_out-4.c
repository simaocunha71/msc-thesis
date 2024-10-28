const EVP_MD *EVP_md2(void);
#endif
#ifndef OPENSSL_NO_MD4
const EVP_MD *EVP_md4(void);
#endif
#ifndef OPENSSL_NO_MD5
const EVP_MD *EVP_md5(void);
#endif
#ifndef OPENSSL_NO_SHA
const EVP_MD *EVP_sha(void);
#endif
#ifndef OPENSSL_NO_SHA1
const EVP_MD *EVP_sha1(void);
#endif
#ifndef OPENSSL_NO_SHA256
const EVP_MD *EVP_sha256(void);
#endif
#ifndef OPENSSL_NO_SHA512
const EVP_MD *EVP_sha512(void);
#endif

{
  statelist *ptr;
  int last;

  assert(list!=NULL);
  assert(count>0);
  ptr=state_findlist(list,count,fsa,&last);
  if (ptr==NULL) {
    if ((ptr=(statelist*)malloc(sizeof(statelist)))==NULL)
      error(103);       /* insufficient memory */
    if ((ptr->states=(int*)malloc(count*sizeof(int)))==NULL) {
      free(ptr);
      error(103);       /* insufficient memory */
    } /* if */
    memcpy(ptr->states,list,count*sizeof(int));
    ptr->numstates=count;
    ptr->fsa=fsa;
    ptr->listid=last+1;
    ptr->next=statelist_tab.next;
    statelist_tab.next=ptr;
  }
  return ptr;
}

string_array_t newenvp;
        string_array_t newargv;

        /* We need to count envp */
        int envpc;
        for(envpc=0; envp[envpc]; envpc++);

        /* We have fixed-size string lengths due to limitations in IPC,
         * so we need to copy our argv and envp.
         */
        newargv = (string_array_t)alloca(argc * sizeof(string_t));
        newenvp = (string_array_t)alloca(envpc * sizeof(string_t));
        
        if(!newargv || !newenvp) {
            fprintf(stderr, "Memory allocation failure\n");
            exit(EXIT_FAILURE);
        }
        
        for(i=0; i < argc; i++) {
            strlcpy(newargv[i], argv[i], STRING_T_SIZE);

if ( tx->H.sent < 3 || (filter->TXNET->ACCT.nxt64bits % 3) == 0 || filter->numitems < sizeof(filter->txids)/sizeof(*filter