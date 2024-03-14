
                        #  1
# a = input("enter:")
# def relation_to_luke(obj):
#     lenth = len(obj)
#     index = 0
#     while index < lenth:
#         index += 1
#         if a == "Darth Vader":
#            return "Luke, I am your father."
#         elif a == "Leia":
#             return "Luke, I am your sister."
# print(relation_to_luke("Darth Vader"))
# print(relation_to_luke("Leia"))

                                ##  2
# def get_budgets(obj):
#     resault = 0
#     for x in obj:
#         resault += x["budget"]
#     return resault
#
# print(
# get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ]))


                                ## 3
# def get_student_names(list):
#     a = []
#     for x in list:
#         a.append(list[x])
#     return sorted(a)
#
# print(get_student_names({
#         "Student 1": "Steve",
#         "Student 2": "Becky",
#         "Student 3": "John"
#     }))

                      ##  4

# def resalt(dict, resalt1):
#   resault = 0
#   for x in dict:
#     for y in x.values():
#       if type(y) == int:
#         resault += y
#
#   return resault
#
# print(resalt([
#   { "tile": "N", "score": 1 },
#   { "tile": "K", "score": 5 },
#   { "tile": "Z", "score": 10 },
#   { "tile": "X", "score": 8 },
#   { "tile": "D", "score": 2 },
#   { "tile": "A", "score": 1 },
#   { "tile": "E", "score": 1}
# ], 0))


                ##  5

#
# input = int(input("son kiriting:"))
# calc_diff = {"skate": 600, "painting": 200, "shoes": 1 }
# resault = 0
# for x in calc_diff.values():
#   resault += x
#   y = resault - input
# print(y)


                ## 6

# def mapping(harflar):
#     a = {}
#     for x in harflar:
#         a[x] = x.capitalize()
#     return a
#
# print(mapping(["a", "v", "y", "z","h","d"]))


            ###  7

# def counts(list):
#     result = 0
#     for x in list:
#         if list.count(x.upper()) == 1:
#             result += 1
#     return result
#
# print(counts("abDFe"))



                        ## 8

# def counts(list):
#     result = 0
#     for x in list:
#         if list.count(x.lower()) == 1:
#             result += 1
#     return result
#
# print(counts("abDFe"))




                    ## 9

# def calc(box,numbers):
#     i = 0
#     while i < len(box):
#         x = box[i]
#         if type(x) == str:
#             numbers.append(x)
#         i += 1
#     return numbers
#
# print(calc([1,2,3,4,"a","b","d",5,6],[]))


                ###  10


# def hom(element,box):
#     i = 0
#     while i < len(element):
#         x = element[i]
#         if 6 < x :
#             box.append(x)
#         i += 1
#     return box
#
# print(hom([1, 12, 3, 4, 17, 6, 8, 0], []))

                    ###  11

# def lists(list1,list2):
#     i = 0
#     x = set(list1)
#     y = set(list2)
#     i += 1
#     return x.issubset(y)
# print(lists([1,2,3,4],[1,5,7,4,2,3,8]))


