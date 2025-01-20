from smartphone import Smartphone

catalog = []

phone_1 = Smartphone("Poco ", "001   ", "+7987654321")
phone_2 = Smartphone("Mi   ", "002   ", "+7123456789")
phone_3 = Smartphone("Apple", "6     ", "+7963258741")
phone_4 = Smartphone("Apple", "11    ", "+79517536482")
phone_5 = Smartphone("XaoMi", "zeta02", "+95147854587")

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

for Smartphone in catalog:
    print (f"{Smartphone.mark} | {Smartphone.model} | {Smartphone.number}")