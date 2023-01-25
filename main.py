from Cat import Cat
from Data import Data


# cat = Cat()
# print(f"Name is currently {cat.getName()}")

# cat.setName("Garfield")
# print(f"Name has been changed to {cat.getName()}")

# data = Data("database")

# data.insert("Cat", cat)

cat = Cat("Garfield")
print(f"Name is currently {cat.getName()}")
print(f"Age is currently {cat.getAge()}")

cat.setName("Tom")
print(f"Name has been changed to {cat.getName()}")
print(f"Previous names: {cat.getNames()}")
print(f"Average name length: {cat.getAverageNameLength()}")

cat.speak()
cat.speak("Hello, I am a cat.")

