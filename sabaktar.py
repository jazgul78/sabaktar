Основы Python
Введение в написание программ
Программа на языке Python состоит из набора инструкции.Каждая инструксия помещется на новую строку.Например:
1) print(2+3)
2) print("Hello")
Больщую роль в Python играют отступы. Неправильно поставленный отступ фактически является ошибкой. Например,в следующем мы получим ошибку,хотя код будет практически аналогичен приведенному выше:
1)print(2+3)
2)	print("Hello")
Поэтому стоит помещать новые инструкции сначала строки. В этом одно из важных отличий пайтона от других языков программирования, как C\\ или Java.
Однако стоит учитывать, что некоторые конструкции языка могут состаять из нескольких строк. Например, условная конструкция if:
1) if 1<2:
2)	print("Hello")
В данном случае если 1 меньше 2,то выводится строка "Hello". И здесь уже должно быть отступ, так как инструкция print ("Hello") используется не сама по себе, а как часть условной конструкции if: Причем отступ, согласно руковотству по оформлению кода, желательно делать из такого количество пробелов, которое кратно 4(то есть 4,8,16 и т.д.) Хотя если отсупов будет работать. 
Таких конструкций не так много, поэтому особой путаницы по поводу где надо,а где ненадо ставить пробелы,не должно возникнуть.s