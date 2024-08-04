item_prices=[10,20,100,500,600]
total_budget=1000
total_count=0
for current_item in item_prices:
    total_budget -=current_item
    if total_budget<0:
        break
    total_count +=1

print(total_count)