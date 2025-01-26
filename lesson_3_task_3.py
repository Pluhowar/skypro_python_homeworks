from address import Address
from mailing import Mailing

to_address = Address("112233", "Moskow", "Lenina", "1", "22")
from_address = Address("223355", "Omsk", "Putina", "12", "92")
mailing = Mailing(to_address, from_address, 100, "A_1")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.house} -{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")