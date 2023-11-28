from monotonic_stack import monotonic_stack as ms


A = ms.MonotonicStack([1, 2, 3, 4, 5])
print(A.next_smaller_on_left())