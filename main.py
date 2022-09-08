# # 0(n^2) time | 0(n) space
# def arrayOfProducts(array):
#     product = [1 for _ in range(len(array))]
#
#     for i in range(len(array)):
#         runningProduct = 1
#         for j in range(len(array)):
#             if i != j:
#                 runningProduct *= array[j]
#         product[i] = runningProduct
#
#     return product

"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangeable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

#
# def getItemClassiness(item):
#     if item == "tophat":
#         return 2
#     elif item == "bowtie":
#         return 4
#     elif item == "monocle":
#         return 5
#     else:
#         return 0
#
#
# class Classy(object):
#     def __init__(self):
#         self.items = []
#
#     def addItem(self, item):
#         self.items.append(item)
#
#     def getClassiness(self):
#         total = 0
#         for item in self.items:
#             total += getItemClassiness(item)
#         return total
#
#
# # Test cases
# me = Classy()
#
# # Should be 0
# print(me.getClassiness())
#
# me.addItem("tophat")
# # Should be 2
# print(me.getClassiness())
#
# me.addItem("bowtie")
# me.addItem("jacket")
# me.addItem("monocle")
# # Should be 11
# print(me.getClassiness())
#
# me.addItem("bowtie")
# # Should be 15
# print(me.getClassiness())

# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


# def show_excitement():
#     # Your code goes here!
#     word = "I am super excited for this course! \n"
#
#     sentence = word * 5
#
#     return sentence
#
#
# print(show_excitement())
