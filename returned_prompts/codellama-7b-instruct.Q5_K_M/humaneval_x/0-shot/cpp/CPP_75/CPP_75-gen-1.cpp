/*
Write a function that takes a string and returns the string where all the 
upper case letters have been changed to lower case and all the lower case letters have been changed to upper case. 
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<ctype.h>
#include<math.h>
#include<stddef.h>
#include<limits.h>
#include<time.h>
#include<assert.h>
#include<setjmp.h>
#include<stdint.h>
#include<errno.h>
#include<stdalign.h>
#include<wchar.h>
#include<complex.h>
#include<uchar.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<sys/ioctl.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<sys/sem.h>
#include<sys/shm.h>
#include<sys/socket.h>
#include<sys/time.h>
#include<sys/utsname.h>
#include<sys/wait.h>
#include<dirent.h>
#include<fnmatch.h>
#include<ftw.h>
#include<glob.h>
#include<libgen.h>
#include<poll.h>
#include<pthread.h>
#include<syslog.h>
#include<unistd.h>
#include<utime.h>
#include<wordexp.h>

bool string_transformer(char *str){
    char *ptr = str;
    char *end = str + strlen(str);
    while(ptr < end){
        if(isupper(*ptr)){
            *ptr = tolower(*ptr);
        }
        else if(islower(*ptr)){
            *ptr = toupper(*ptr);
        }
        ptr++;
    }
    return false;
