# 10 - misol
import math
#
sonlar = [4, 9, 16, 25]
ildizlar = [math.sqrt(x) for x in sonlar]

print(ildizlar)

#11 - misol
bolinish = [x for x in range(50) if x % 5 ==0]
print(bolinish)

#12 - misol
my_list = ["hello", "world", "python"]
bosh_harf = [x.capitalize() for x in my_list]
print(bosh_harf)
