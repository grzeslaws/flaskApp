# loremListSlice = []

# with open("lorem.txt") as lorem:
#     loremList = lorem.read().split(" ")
#     numberOfWords = int(input("Enter numver of words: "))
#     loremListSlice = loremList[0:numberOfWords]

# with open("write.txt", "w") as write:

#     loremListSlice = map(lambda n: n + " ", loremListSlice)
#     write.write("".join(loremListSlice))


class GetWords:

    fromFile: str
    destFile: str
    numberOfWords: int
    loremListSlice: str

    @classmethod
    def enterValue(cls):
        cls.fromFile = input("Enter from file: ")
        cls.destFile = input("Enter dest file: ")
        cls.numberOfWords = int(input("Enter number 0f words: "))
        with open(cls.fromFile) as lorem:
            loremList = lorem.read().split(" ")
            cls.loremListSlice = loremList[0:cls.numberOfWords]
        
        with open(cls.destFile, "w") as write:
            cls.loremListSlice = map(lambda n: n + " ", cls.loremListSlice)
            write.write("".join(cls.loremListSlice)) 

getWords = GetWords()
getWords.enterValue()

# with open("write.txt", "w") as write_f:
#     write_f.write("Velit rerum quos sapiente veniam labore qui, ex adipisci")
#     write_f.write("\nquos sapiente veniam labore qui, ex adipisci")
#     write_f.write("\nquos sapiente veniam labore qui, ex adipisci")


# with open("lorem.txt") as lorem:
#     loremLines = lorem.readlines()

#     loremLinesFiltered = list(filter(lambda n: "Lorem" not in n, loremLines))
#     print(loremLinesFiltered)


# lorem = open("lorem.txt")

# for line in lorem:
#     print(line)
# class Tab:

#     menu = {
#         "pizza": 32,
#         "soup": 20,
#         "cola": 5
#     }

#     def __init__(self):
#         self.total = 0
#         self.items = []

#     def add(self, item):
#         self.items.append(item)
#         self.total += self.menu[item]

#     def bill(self):

#         for i in self.items:
#             print(f"Ordered items: {i:20} amount: {self.menu[i]}")

#         print(f"Total: {self.total: 20}")


# tab = Tab()

# tab.add("pizza")
# tab.add("soup")
# tab.add("cola")

# tab.bill()


# class Person:

#     lastName = "kowalsky"

#     def __init__(self, color, firstName):
#         self.color = color
#         self.firstName = firstName

#     def printColor(self):
#         print(self.color)

#     @classmethod
#     def printLastName(cls):
#         print(cls.lastName)

#     @staticmethod
#     def staticMethod(col):
#         print(f"Color is: {col}")


# person = Person("blue", "Sam")

# print(f"Person color is: {person.firstName}")
# person.staticMethod("white")


# def ninja_intro(dict):
#     for key, val in dict.items():
#         print(f'I am {key} and I am a {val} belt')

# ninja_belts = { }

# while True:
#     ninja_name = input('add a ninja name: ')
#     ninja_belt = input('add a ninja colour: ')
#     ninja_belts[ninja_name] = ninja_belt

#     another = input('add another? (y/n): ')
#     if another == 'y':
#         continue
#     else:
#         break

# ninja_intro(ninja_belts)
