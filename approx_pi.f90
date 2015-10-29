subroutine approx_pi(intervals, pi)
  integer, intent(in) :: intervals
  double precision, intent(out) :: pi
  integer i
  pi = 0
  do i = 0, intervals - 1
     pi = pi + (4 - (mod(i,2) * 8)) / dble(2 * i + 1)
  enddo
end subroutine approx_pi

