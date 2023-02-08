def list_partitions(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_m = []
        if n == m:
            exact_m = [[m]]
        with_m = [p + [m] for p in list_partitions(n-m, m)]
        without_m = list_partitions(n, m-1)
        return exact_m + with_m + without_m