from itertools import combinations
a=[1,-2,3,4,-3,0,5]
print("Positive Combinations")
for r in range(1,len(a)+1):
    for combo in combinations(a,r):
        if all(num>0 for num in combo):
            print(combo)


        
