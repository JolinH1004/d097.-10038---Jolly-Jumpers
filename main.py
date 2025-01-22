try:
    while True:
        n = list(map(int,input().split(' '))) # list轉int。不可list()換成[]
        n_len = n[0]
        b = [] # 儲存兩者相差的數，有n-1個
        
        for i in range(1, n_len+1):
            if i == 1:
                continue
            else:
                d = n[i] - n[i-1]
                if d < 0:
                    d = -d
                b.append(d)
        
        # 1. 重複數字 2.數字 > n-1
        for i in range(1, n_len):
            if i in b:
                if b.count(i) > 1: # 1.
                    print('Not jolly')
                    break
                b.remove(i)
                if b == []:
                    print('Jolly')
            else: # 2. 考慮(d > n-1)
                print('Not jolly')
                break
except EOFError:
    pass

