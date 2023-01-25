from Cat import Cat
from Dog import Dog

def saveTest():
    cat = Cat("Whiskers")
    data.insert("Cat", cat)
    
    dog = Dog("Fido")
    data.insert("Dog", dog)

def savePetShop():
    data.beginTran()
    cats = [Cat() for i in range(3)]
    dogs = [Dog() for i in range(3)]
    try:
        for cat in cats:
            data.insert("Cat", cat)
        for dog in dogs:
            data.insert("Dog", dog)
        data.commit()
    except:
        data.rollback()

def logStats():
    print(f"Number of cats inserted: {len(cats)}")
    print(f"Number of dogs inserted: {len(dogs)}")

data = Data("database")
saveTest()
savePetShop()
logStats()
