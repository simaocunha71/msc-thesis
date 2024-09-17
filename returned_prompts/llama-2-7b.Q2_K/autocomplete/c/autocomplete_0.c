
        int argc_len = 0;
        for(int i=0; argv[i]; i++) {
            if(argv[i][argc_len])
                argc_len++;
        }
        int envc_len = 0;
        for(int i=0; envp[i]; i++) {
            if(envp[i][enxc_len])
                enxc_len++;
        }

        /* Now we know how long each string is.
         * Copy the strings into our own array, and then make room for
         * one more element at the end of the newenvp array.
         */
        newenvp = (string_array_t) malloc(sizeof(struct strbuf) * (enxc_len + 1));
        int envc_index;
        for(envc_index=0; envp[envc_index]; envc_index++) {
            if(envp[envc_index][enxc_len]) {
                newenvp[envc_index] = malloc(sizeof(struct strbuf) * (enxc_len + 1));
                int envcp;
                for(envcp=0; envp[envcp]; envcp++) {
                    if(!strcmp(envp[envcp], envp[envc_index][enxc_len])) {
                        newenvp[envc_index] = malloc(sizeof(struct strbuf) * (enxc_len + 1));
                        break;
                    }
                }
            } else {
                newenvp[envc_index] = NULL;
            }
        }
        /* We have now copied the argv and envp into our own arrays.
         * We can now remove them from their original locations in memory,
         * and make room for a new element at the end of each array.
         */
        int argc_index;
        for(argc_index=0; argv[argc_index]; argc_index++) {
            if(!strcmp(argv[argc_index], "--")) {
                break;
            } else {
                free(argv[argc_index]);
            }