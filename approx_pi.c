double approx_pi(int intervals)
{
     double pi = 0.0;
     int i;
     for (i = 0; i < intervals; i++) {
         pi += (4 - ((i % 2) * 8)) / (float)(2 * i + 1);
     }
     return pi;
}

