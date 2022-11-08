# Dictionary or JSON
#
# customer = {
#     "name" : "john",
#     "age" : 23,
#     "is_verified" : True
# }
# customer["name"] = "John Smith"
# print(customer["name"])

#convert number to string
# phone = input("phone: ")
# digit_mapping = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four"
# }
# output = ""
# for ch in phone:
#     output += digit_mapping.get(ch, "!") + " "
# print(output)

#Emojis Converter
message =input(">")
words = message.split(' ')
emojis = {
    ":)" : "😀",
    ":(" : "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)