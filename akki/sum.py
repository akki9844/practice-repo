s=[1,2,3,4,5,6,7,8]
d={}
for i in s:
    if i in d.keys():
        d[i]=d[i]+1

    else:
        d[i]=1
for k,v in d.items():
    print('{}={} '.format(k,v))
    print()