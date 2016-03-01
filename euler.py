my_func = lambda t, x : t * x + t

def findValue(x0, t0, tN, N):
    h = (tN-t0)/N
    x_list = []
    t_list = []
    x,t = x0, t0
    for i in range(N):
        curr = x  + h * my_func(t,x)
        x_list.append(curr)
        t_list.append(t)
        t += h
        x = curr
    return x_list, t_list

print findValue(1, 0, 1, 4)