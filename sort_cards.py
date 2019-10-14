# -*- coding: utf-8 -*-
#(黑桃)表示为$ ; (红桃)表示为&;(梅花)表示为* ;(方块)表示为# .
#数字大小顺序：  2、3、4、5、6、7、8、9、10、J、Q、K、A
TestList = ['&K', '$A', '$6', '$3', '#3', '&6', '*4', '#2', '*K', '#9', '#8', '#8', '#9']
dict = {
        '#2':1,'#3':5,'#4':9,'#5':13,'#6':17,'#7':21,'#8':25,'#9':29,'#10':33,'#J':37,'#Q':41,'#K':45,'#A':49,
        '*2':2,'*3':6,'*4':10,'*5':14,'*6':18,'*7':22,'*8':26,'*9':30,'*10':34,'*J':38,'*Q':42,'*K':46,'*A':50,
        '&2':3,'&3':7,'&4':11,'&5':15,'&6':19,'&7':23,'&8':27,'&9':31,'&10':35,'&J':39,'&Q':43,'&K':47,'&A':51,
        '$2':4,'$3':8,'$4':12,'$5':16,'$6':20,'$7':24,'$8':28,'$9':32,'$10':36,'$J':40,'$Q':44,'$K':48,'$A':52,
        }
#排序所用函数
def cmp(a, b):
    if dict[b] < dict[a]:
        return 1
    if dict[a] < dict[b]:
        return -1
    return 0
TestList = sorted(TestList, key=functools.cmp_to_key(cmp))
