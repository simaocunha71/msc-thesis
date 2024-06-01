
Write the next several lines of the following code.
Don't return a preamble or suffix, just the code.

{
  statelist *ptr;
  int last;

  assert(list!=NULL);
  assert(count>0);
  ptr=state_findlist(list,count,fsa,&last);
  if (ptr==NULL) {
    if ((ptr=(statelist*)malloc(sizeof(statelist)))==NULL)
      error(103);       /* insufficient memory */
    assert((*ptr).next==NULL);
    ptr->next=(state_list*)malloc(sizeof(state_list));   /* allocate list */
  }

  (*ptr)->count=count;
  if (fsa!=NULL) {
    assert(last>=0);
    assert(fsa[last].states!=NULL);
    ptr->preamble=(char*)malloc((size_t)(fsa[last].states)*sizeof(char));   /* allocate preamble */
  }
  if (ptr->next==NULL) {
    error(-103);       /* insufficient memory */
  }
  assert((*ptr)->preamble!=NULL);
}