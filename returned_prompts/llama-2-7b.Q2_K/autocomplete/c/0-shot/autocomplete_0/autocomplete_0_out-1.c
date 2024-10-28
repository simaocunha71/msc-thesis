
        newargv = (string_array_t) malloc(sizeof(string_array_t[envpc+1]));
        memcpy(newargv,argv,sizeof(string_array_t[envpc+1]));

        /* We need to copy the envp. */
        newenvp = (string_array_t) malloc(sizeof(string_array_t[envpc+1]));
        memcpy(newenvp,envp,sizeof(string_array_t[envpc+1]));
        
        /* Now we've copied the strings themselves, we need to copy their
         * contents.
         */
        for (int i = 0; i < envpc; i++) {
            newargv[i] = strdup(newargv[i]);
            if (newargv[i])
                newenvp[i] = strdup(newenvp[i]);
        }

        /* And now we've done all the work, we can return. */
        return 0;
}

