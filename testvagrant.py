newspapers=['TOI','Hindu','ET','BM','HT']
prices=[26,20.5,34,10.5,18]

def subscriptions(newspapers,prices,budget):
    l=len(newspapers)
    ans=[]
    for i in range(l):
        for j in range(i+1,l):
            if prices[i]+prices[j]<=budget:
                ans.append({newspapers[i],newspapers[j]})
    return ans
    
budget=int(input("enter weekly budget:"))
print(subscriptions(newspapers,prices,budget))
