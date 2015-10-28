#include <math.h>
#include <time.h>
#include <stdio.h>

double approx_pi(int intervals)
{
     double pi = 0.0;
     int i;
     for (i = 0; i < intervals; i++) {
         pi += (4 - ((i % 2) * 8)) / (float)(2 * i + 1);
     }
     return pi;
}

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
