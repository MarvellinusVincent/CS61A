def str_partitions(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_m = []
        if n == m:
            exact_m = [str(m)]
        with_m = [p + " + " + str(m) for p in str_partitions(n-m, m)]
        without_m = str_partitions(n, m-1)
        return exact_m + with_m + without_m