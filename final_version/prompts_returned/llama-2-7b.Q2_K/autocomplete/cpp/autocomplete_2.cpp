
Write the next several lines of the following code.
Don't return a preamble or suffix, just the code.


        strcat(name, "%0");

        int i;
        char *extension;
        for(i = 0, extension = at; isdigit(at[i]); i++, extension++)
            ;
        char places[10];
        sprintf(places, "%dd", i);

        return strcat(name, places);
