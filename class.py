# Задача 17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# a = [1, 1, 2, 0, -1, 3, 4, 4]

# a = set(a)
# print(a)
# a=list(a)
# print(len(a))

# n=[1, 1, 2, 0, -1, 3, 4, 4]
# itog = []
# for i in n:
#     if i not in itog:
#         itog.append(i)
# print (len(itog))










# Задача 19. 
# Дана последовательность из N целых чисел 
# и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, 
# K –положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# n = [1,2,3,4,5]
# k = int(input("k: "))-1
# print(*n[-k:],*n[:len(n)-k])

# n = [1,2,3,4,5]
# k = int(input("k: "))-1
# for i in range(k):
#     n.insert(0,n.pop())
# print(n)





# Задача 21. 
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# a = [{"V": "S001"}, {"V": "S002"},{"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# d = []
# for i in a:
#     for m in i:
#         d.append(i[m])

# print(set(d))





# Задача N23.
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество элементов 
# массива, больших предыдущего (элемента с предыдущим 
# номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)



# a = [0, -1, 5, 2, 3]
# count = 0
# for i in range (len(a)-1):
#     if a[i+1] > a[i]:
#         count+=1
#     i+=1

# print(count)







# Задача №25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# a = str(input())
# a = a.split()
# print(a)
# count=0
# count_temp=0
# b=str(f'{a[0]}')
# temp=a[0]
# for j in range(1,len(a)):
#     if a[j]==a[j-1]:
#         count+=1
#         b=b+str(f' {a[j]}_{count}')
#         temp = a[j-1]
#         count_temp=count
#     elif a[j]==temp:
#         count_temp+=1
#         b=b+str(f' {a[j]}_{count_temp}')
#         count = count_temp
#     else: 
#         count=0 
#         b=b+str(f' {a[j]}')
             
# print(b)


# a = ('a a a b c a a d c d d').split()
# res={}
# a_res =[]
# for i in a:
#     if i not in res:
#         res[i] = 0
#         print (i, end = ' ')
#     else:
#         res[i]+=1
#         print(i,'_',res[i], end = " ")
# list = """ She sells sea shells on the sea shore 
# The shells that she sells are sea shells 
# I'm sure.So if she sells sea
# shells on the sea shore 
# I'm sure that the shells are sea
# shore shells"""
# print(len(set(list.upper().replace('.', ' ').split())))


# Задача 33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# from random import randint

# num = int(input('Введите количество оценок'))
# listOcenok = [randint(1,5) for i in range(num)]

# print(*listOcenok)

# newspisok = []
# for el in listOcenok:
#     if el==max(listOcenok):
#         newspisok.append(min(listOcenok))
#     else:
#         newspisok.append(el)

# print(newspisok)



# Задача 30. Факториал

# n = int(input('Введите n:'))

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return fact(n-1)*n
    
# print(fact(n))



    

# Задача 31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, 
# ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

    
# n = int(input("введите число n:"))
# def fibbo(n):
#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else: 
#             return fibbo(n-1)+fibbo(n-2) 
# print(fibbo(n))







# Задача 35
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n (само число)
# Input: 5
# Output: yes 


n = int(input("введите число n:"))
def simplecheck(n):
                # if n%(n-1)==0:
                #         return print ("yes")
                # elif n!=2:
                #         n=n-1
                #         simplecheck(n)
                # else:
                #         return print ("no")
                   if n%(n-1)==0:
                        return print ("yes")
                    elif n!=2:
                            n=n-1
                            simplecheck(n)
                    else:
                            return print ("no")

simplecheck(n)









# for i in len(a):
#     print (a[i], i)




# list1 = [3, 1, 3, 4, 2, 4, 12]
# l1=set(list1)
# list2 = [4, 15, 43, 1, 15, 1]
# l2=set(list2)
# print(l1.difference(l2))



# Даны два массива чисел. Требуется вывести те 
# элементы первого массива (в том порядке, в каком 
# они идут в первом массиве), 
# которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов
# в первом массиве, затем N чисел - элементы 
# массива. Затем число M - количество элементов 
# во втором массиве. Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
