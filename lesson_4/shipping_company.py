user_area="mohakhali"
total_purchase_price=600
if user_area in ["mirpur","farmgate","dhanmondi"]:
    if total_purchase_price>=600:
        print("shipping is free")
    elif 300<=total_purchase_price<600:
        print("shipping cost 80")
    else:
        print("shipping cost 150")    

#dhanmondi is use in if and elif so if we choce that their could be a overlap.it choese 1st one
elif user_area in ["mohakhali","dhanmondi"]:
    if total_purchase_price >=800:
        print("shipping free")
    elif 500 <=total_purchase_price<800:
        print("shipping 100")
    else:
        print("shipping cost 200")


else:
    print("shipping currently not available")