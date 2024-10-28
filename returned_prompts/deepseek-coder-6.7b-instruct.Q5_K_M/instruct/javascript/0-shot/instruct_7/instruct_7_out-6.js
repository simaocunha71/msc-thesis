
    Your solution should be as concise and efficient as possible.
    */
    char* copy_buffer(int* n, struct BufferList* list){
        if(*n == 0 || list == NULL){
            return NULL;
        }

        struct BufferList* current = list;
        int total_size = 0;
        while(current != NULL && *n > 0){
            total_size += current->size;
            *n -= current->size;
            current = current->next;
        }

        if(*n < 0){
            total_size += *n;
        }

        char* new_buffer = (char*)malloc(total_size);
        if(new_buffer == NULL){
            return NULL;
        }

        current = list;
        char* ptr = new_buffer;
        while(current != NULL && *n > 0){
            memcpy(ptr, current->data, current->size);
            ptr += current->size;
            *n -= current->size;
            current = current->next;
        }

        if(*n < 0){
            memcpy(ptr, current->data, *n);
        }

        return new_buffer;
    }

    /*
    Write a function in C that merges two sorted linked lists into a single sorted linked list. 
    The function should take two arguments: `list1` and `list2`, pointers to the heads of the two linked lists. 
    The function should return a pointer to the head of the merged linked list.
    The linked lists are sorted in ascending order.
    You are not allowed to use any application-specific variables or libraries.
    The function should be inlinable and should be as efficient as possible.
    */
    struct ListNode* merge_sorted_lists(struct ListNode* list1, struct ListNode* list2){
        if(list1 == NULL){
            return list2;
        }
        if(list2 == NULL){
            return list1;
        }

        struct ListNode* head = NULL;
        if(list1->val <