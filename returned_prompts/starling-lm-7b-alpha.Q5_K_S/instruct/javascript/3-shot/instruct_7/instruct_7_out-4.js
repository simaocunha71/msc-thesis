        void *buffer;
        size_t n;

        if ( n > sizeof(buffer) )
            n = sizeof(buffer);

        if ( !Buffer.allocUnsafe((void *)&buffer, n) )
            error(103);       /* insufficient memory */

        for ( i = 0; i < n; i++ )
        {
            buffer = List_pop(list);

            if ( buffer == NULL )
                error(103);       /* insufficient memory */

            memcpy(buffer, List_pop(list), List_size(list));
        }

