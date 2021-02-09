import statistics 
n = int(input())
budget = list()

for i in range(n):
    budget.append(int(input()))
budget.sort()   
max=0
sum=0
for i in budget:
    sum=i*(n)
    if sum>max:
        max=sum
    n=n-1
print(max)
