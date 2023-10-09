/*
 * Análise e Teste de Software
 * João Saraiva
 * 2016-2017
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h>
#include <string.h>
#include "rapl.h"

#define RUNTIME

int main(int argc, char **argv)
{
  char command[500] = "";
  char res[500] = "";
  int ntimes = 1;
  int core = 0;
  int i = 0;

#ifdef RUNTIME
  struct timeval tvb, tva;
#endif
  FILE *fp;

  if (argc < 4)
  {
    fprintf(stderr, "Usage: %s <command> <ntimes> <output_filename>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  strcpy(command, argv[1]);
  printf("Program to be executed: %s\n", command);

  ntimes = atoi(argv[2]);

  strcpy(res, argv[3]);
  strcat(res, ".J");
  printf("Command: %s %d times, Output File: %s\n", command, ntimes, res);

  printf("\n\n RUNNING THE PARAMETRIZED PROGRAM:  %s\n\n\n", command);
  fflush(stdout);

  fp = fopen(res, "w");

  if (fp == NULL)
  {
    perror("Error opening output file");
    exit(EXIT_FAILURE);
  }

  rapl_init(core);

  fprintf(fp, "Program, Package, Core(s), GPU, DRAM?, Time (sec)\n");

  for (i = 0; i < ntimes; i++)
  {
    sleep(1);                     // sleep for 1 second
    fprintf(fp, "%s, ", argv[3]); // write the ID to the csv/.J file
    rapl_before(fp, core);

#ifdef RUNTIME
    gettimeofday(&tvb, NULL);
#endif

    if (system(command) == -1)
    {
      perror("Error executing command");
      exit(EXIT_FAILURE);
    }

#ifdef RUNTIME
    gettimeofday(&tva, NULL);
    double time_spent = (tva.tv_sec - tvb.tv_sec) + (tva.tv_usec - tvb.tv_usec) / 1e6;
#endif

    rapl_after(fp, core);

#ifdef RUNTIME
    fprintf(fp, " %lf\n", time_spent);
#endif
  }

  printf("\n\n END of PARAMETRIZED PROGRAM: \n");

  fclose(fp);
  fflush(stdout);

  return 0;
}
