sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
sales.extend(sales_w1)

sales.extend(sales_w2)

print(max(sales))
 
bestday= float(max(sales))*1.5
worstday= float(min(sales))*1.5


print(bestday) 
print(worstday)

combine = bestday + worstday

print(combine)
total =0
for day in sales:
    earning = day*1.5
    print(earning)
    total = total+earning

    

print(total)


    