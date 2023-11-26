/*
 *  Análise e Teste de Software
 *  João Saraiva
 *  2016-2017
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h> // Include for gettimeofday
#include <string.h>
#include <unistd.h> // Include for sleep
#include "rapl.h"

#define RUNTIME

int main(int argc, char **argv)
{
  char command[500], res[500];
  int ntimes = 1;
  int core = 0;
  int i = 0;

#ifdef RUNTIME
  struct timeval tvb, tva;
#endif

  FILE *fp;

  if (argc < 4)
  {
    fprintf(stderr, "Usage: %s <program_name> <ntimes> <result_prefix>\n", argv[0]);
    return 1;
  }

  strcpy(command, "");
  strcat(command, argv[1]);
  //printf("Program to be executed: %s\n", argv[1]);

  ntimes = atoi(argv[2]);

  strcpy(res, argv[3]);
  strcat(res, ".J");
  //printf("Command: %s  %d-times res: %s\n", command, ntimes, res);

  printf("\n\n RUNNING THE PARAMETRIZED PROGRAM:  %s\n\n\n", command);
  fflush(stdout);

  fp = fopen(res, "w");
  if (strlen(res) >= 2)
  {
    res[strlen(res) - 2] = '\0';
  }
  rapl_init(core);

  fprintf(fp, "Program,Package,Core,GPU,DRAM,Time\n");

  for (i = 0; i < ntimes; i++)
  {
    sleep(1);                  // sleep 1 second
    fprintf(fp, "%s , ", res); // NOTE: retirar o .J da string que vai ser adicionada ao .J
    rapl_before(fp, core);

#ifdef RUNTIME
    gettimeofday(&tvb, 0);
#endif

    system(command);

#ifdef RUNTIME
    gettimeofday(&tva, 0);
    double time_spent = (tva.tv_sec - tvb.tv_sec) + (tva.tv_usec - tvb.tv_usec) / 1e6; // NOTE: Time in seconds
#endif

    rapl_after(fp, core);

#ifdef RUNTIME
    fprintf(fp, " %lf \n", time_spent);
#endif
  }

  printf("\n\n END of PARAMETRIZED PROGRAM: \n");

  fclose(fp);
  fflush(stdout);

  return 0;
}
