def partitions(n, m):
    if n < 0 or m == 0:
        return []
    else:
        if n == m:
            yield str(m)
        for p in partitions(n-m,m):
            yield p + " + " + str(m)
        yield from partitions(n, m-1)
