def shop(gift):
    # print("Red color")
    gift()
    return shop

@shop
def gift():
    print("Red color")

gift()    