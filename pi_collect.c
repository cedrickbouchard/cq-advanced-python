#include <math.h>
#include <time.h>
#include <stdio.h>
#include "approx_pi.h"

int main(int argc, char *argv[])
{
    clock_t t1 = clock();
    double pi = approx_pi(100000000);
    clock_t t2 = clock();
    printf("PI is approximately %.16f, Error is %.16f\n",
	   pi, fabs(pi - M_PI));
    printf("Time = %.16f sec\n", (double)(t2 - t1)/CLOCKS_PER_SEC);
    return 0;
}
