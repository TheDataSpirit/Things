import time as ding
def raiseTo(nu,p):
  return nu**p
n=1
v=6
print("These are the squares until",v,sep=None)
for n in range(1,v+1,1):
  print(n,"squared is",raiseTo(n,2))
  ding.sleep(1)
