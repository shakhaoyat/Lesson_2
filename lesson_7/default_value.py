def calculate_net(total_price,tax=5):
    net_price=total_price+total_price*(tax/100)
    print(net_price)

calculate_net(100)
calculate_net(300)
calculate_net(400)
calculate_net(100,20)