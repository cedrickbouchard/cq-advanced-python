import math
import time
import sys
approx_pi = __import__(sys.argv[1])

t1 = time.clock()
pi = approx_pi.approx_pi(int(sys.argv[2]))
t2 = time.clock()
print("PI is approximately %.16f, Error is %.16f"%(pi, abs(pi - math.pi)))
print("Time = %.16f sec\n"%(t2 - t1))
