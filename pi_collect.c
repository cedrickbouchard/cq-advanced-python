#include <math.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include "approx_pi.h"

int main(int argc, char *argv[])
{
    clock_t t1 = clock();
    int n = atoi(argv[1]);
    double pi = approx_pi(n);
    clock_t t2 = clock();
    printf("PI is approximately %.16f, Error is %.16f\n",
	   pi, fabs(pi - M_PI));
    printf("Time = %.16f sec\n", (double)(t2 - t1)/CLOCKS_PER_SEC);
    return 0;
}
