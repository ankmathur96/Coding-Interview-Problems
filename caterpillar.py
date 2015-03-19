def count_uneaten(n, A):
    n_leaves = n
    count = 1
    lst = []
    while count <= n:
        eaten = False
        for divisor in A:
            if count % divisor == 0:
                eaten = True
                break
        if eaten:
            n_leaves = n_leaves-1
        count += 1
    return n_leavess