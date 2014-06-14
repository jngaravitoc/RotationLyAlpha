#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define NPOINTS 1000
#define TEMP 10000
#define USAGE "analytic_solution.x tau velocity(km/s) viewing_angle(degrees)"

/*
  This codes computes an analytic solutions for the Lya radiation 
  transfer problem of a rotating sphere.

  The solution was computed by Mark Dijsktra and is published in the 
  paper: Garavito-Camargo, Forero-Romero, Dijstra, ApJ ....

  Author: Jaime E. Forero-Romero (Uniandes)
  Creation date: 14-Jun-2014

  Modifications:
*/


int main(int argc, char **argv){
  int i;
  float *x;
  if(argc!=4){
    fprintf(stderr, "USAGE: %s\n", USAGE);
  }
    
  return 0;
}
