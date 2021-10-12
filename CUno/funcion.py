def computepay(h,r):
    if h <= 40:
        res = h*r
        return res
    else:
        dif = h-40
        r2 = r+r/2
        res = (40*r)+(dif*r2)
        return res

hrs = input("Enter Hours:")
rat = input("Enter tar:")
h = float(hrs)
r = float(rat)
p = computepay(h,r)
print("Pay",p)
