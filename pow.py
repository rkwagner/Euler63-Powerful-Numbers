tot = 0
for n in range(1, 10):
    for k in range(1, 30):
        num = n**k
        if len(str(num)) == k:
            tot += 1
print "Total powerful numbers: ", tot
