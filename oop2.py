class Appartment(object):
    def __init__(self, price: int, space: int, rooms: int):
        self.price = price
        self.space = space
        self.rooms = rooms

    def __repr__(self):
        return "<Appartment price:%s, space:%s, rooms:%s>" % (self.price, self.space, self.rooms)

    def __str__(self):
        return "Appartment price:%s, space:%s, rooms:%s" % (self.price, self.space, self.rooms)


def search_by_rooms(arr, rooms):
    return list(filter(lambda x : x.rooms == rooms, arr))


def search_by_max_price(arr, max_price):
    return list(filter(lambda x : x.price <= max_price, arr))

    
def search_by_space(arr, space):
    min_space = int(space - (space * 10 / 100))
    max_space = int(space + (space * 10 / 100))
    return list(filter(lambda x : x.space in range(min_space, max_space), arr))


appartments = list()
appartments.append(Appartment(10000, 22, 1))
appartments.append(Appartment(20000, 40, 1))
appartments.append(Appartment(25000, 43, 2))
print(search_by_rooms(appartments, 1))
print(search_by_max_price(appartments, 25000))
print(search_by_space(appartments, 40))