numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
primes = []
not_primes = []
for i in numbers:
    for j in range(2, i):
        #flag = True
        #type(j) == int
        if i % j == 0:
            not_primes.append(i)
        else:
            flag = False
        break
    #i >= j
    #j = numbers [i]
    #if  i % j == 0:
     #primes [i]
     #print (primes[i])
    #else:
     # primes[i]
print (not_primes)