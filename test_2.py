# Q1
number_1 = input("Bir sayı giriniz")
if number_1.isnumeric() == False :

   print('bu değer toplamak için uygun değil, lütfen tekrar deneyin')
else:
   number_1 = float(number_1)
   number_2 = input("İkinci sayıyı giriniz")

   if number_2.isnumeric() == False :
     print('bu değerler toplamak için uygun değil, lütfen tekrar deneyiniz')

   elif number_2.isnumeric() == True:
     number_2 = float(number_2)
     print(number_1 + number_2)


# Q2
number_1 = input('bir sayı giriniz')
if number_1.isnumeric() == False:
  print('bu bir sayı değil.')
else:
  number_1 = float(number_1)
  number_2 = input('ikinci sayı giriniz')
  if number_2.isnumeric() == False:

      print('bu bir sayı değil')
  else:
      number_2 = float(number_2)
      secenek_1 = input('seçeneği giriniz')
      secenek_1=float(secenek_1)
      if secenek_1==0:
         print(number_1 + number_2)
      elif secenek_1==1:
         print( number_1 - number_2)
      elif secenek_1== 2:
         print( number_1 * number_2)
      else:
         print('Böyle bir seçenek yok')

# Q3
text = """
Lorem ipsum dolor sit amet 34 consectetur adipiscing elit Integer 22 massa nulla bibendum id accumsan id 78 
convallis dictum enim Phasellus lorem metus pretium vulputate rutrum in rutrum sed tortor 1 Fusce ultrices aliquet
nibh porttitor lacinia 6 Suspendisse fermentum condimentum sollicitudin 443 Pellentesque habitant morbi tristique
senectus et netus et malesuada fames ac turpis egestas 8 Duis feugiat ultricies sapien sit amet semper Vivamus 
id purus eros Etiam elit leo tincidunt eu justo eget 123 aliquam imperdiet velit Nullam in diam nulla

Fusce vitae erat ac ipsum pulvinar elementum 1536 Morbi ipsum quam accumsan ac lorem nec condimentum bibendum
massa Etiam tortor lacus 9087 commodo eu lectus non 543 mollis egestas odio Sed non lacinia risus In ultricies
varius arcu 5 sit amet tempus mi ullamcorper in 87 Proin tempor ornare sem 2 nec vehicula turpis varius id Etiam
nec euismod magna Sed tempus in mi vel porta 78 Praesent mauris nisl elementum at justo in condimentum ultrices
turpis

Vestibulum malesuada eleifend dignissim Sed tincidunt ligula eu augue ornare pellentesque 984 Donec lacus risus
pulvinar a velit eget pellentesque dapibus orci Etiam in turpis lorem Suspendisse fermentum quam a justo sollicitudin
fringilla 3223 Quisque purus purus dictum pellentesque ullamcorper nec sodales id tortor Integer mollis bibendum
orci et convallis Mauris viverra quam nec convallis ullamcorper 423 Etiam nec dui lobortis rhoncus ante nec 457
venenatis justo Curabitur ullamcorper ligula lacus at ullamcorper neque varius in Nulla pulvinar ultricies
sodales Integer pretium tempor libero 1211 non pellentesque quam dapibus ac Vivamus ultricies luctus tincidunt
Integer nisi justo 287 hendrerit id libero luctus sollicitudin dapibus sem Proin vel nisi hendrerit laoreet nulla
id 999 rhoncus nisl
"""
#regex kullanmadan yapamadım o yüzden bu soru da boş


# Q4
f = open("text.txt", "r")
print (f.read())

#numaraları replace etmeden nası bulcağımı bilmiyorum o yüzden bu soru yarım

# Q5
array = [['Ahmet Yılmaz', '05136462233'], ['Büsra Sert', '05221115568'], ['Öznur Hakkı', '05125468800'],
         ['Mehmet Dal', '06771224567'], ['Melike Aynur', '05216750076'], ['Uğur Kaplan', '05235467733']]
s = dict(array)
print(s)

# Q6
f = open("rehber.txt", "r")
isim = input('bir isim giriniz')
# f.readline()
# if isim == 'Ahmet Yılmaz' :
#     print(f.readline())
#
# elif isim == 'Busra Sert' :
#     print(f.readline())

for i in f.readlines():
    ad = i
    if isim.lower() in i.lower():
        print(i)
        break

program = input("lütfen 1. veya 2. seçeneği seçiniz")

if program =='1' :
    s = input("isim soy isimi giriniz")

    with open("rehber.txt", "a") as f:
        f.write(s)
    l = input("numarayı giriniz")

    with open("rehber.txt", "a") as f:
        f.write(l)

elif program =='2' :
    input('bir isim giriniz ')
    f = open("rehber.txt", "r")
    for i in f.readlines():
        ad = i
        if isim.lower() in i.lower():
            print(i)
            break
