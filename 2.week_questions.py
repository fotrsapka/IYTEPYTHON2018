# Q1 Kullanıcıdan sayı alın iki tane. ve bu sayıları toplayın ve ekrana yazdırın. Eğer sayılar int e çevirmeye uygun
#  değil ise ekrana Bu değerler toplamak için uygun değildir diye ekrana yazdırın. uygunsa sayıları toplayıp
# ekrana yazdırın. input() ile alabilirsiniz kullanıcıdan girdi.


# Q2 kullanıcıdan iki tane sayı alın ve bir tane de ayrı bir sayı alın ve buna seçenek deyin. Eğer seçenek 0 ise
# iki sayıyı toplasın 1 ise çıkarsın 2 ise çarpsın 3 ise bölsün, hiçbiri değil ise Böyle bir seçenek yok diye ekrana
# yazsın. Çıkan sonuçları da ekrana yazdırmayı unutmayın. Ve yine bu sayılar int e çevirmeye uygun değilse ekrana uyarı
# verin

# Q3 Bu textte kaç tane sayı olduğunu bulun. re kütüphanesini kullanmayınız yani regex kullanmayınız.

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

# Q4 Yukarıdaki textin aynısı text.txt adında bir dosyanın içinde var onu okuyun pythonda. 'read file in python'
# ile arayabilirsiniz googlede. daha sonra içindeki numaraları kaldırıp yeni oluşan texti text2.txt adında yeni
# bir dosyaya kaydedin. (Numaraları tek tek bulup replace etmeyin), (Regex kullanmayın)


# Q5 aşağıdaki arrayi dict'e çevirin. dict'in key değeri isim soyisim olsun, value de numara olsun.
# Mesela Ahmet Yılmaz key değeri 05136462233 de o keye karşıkık olan value
# daha sonra dict içindeki Melike Aynur key'ene ait olan value'yi ekrana yazdırın

array = [['Ahmet Yılmaz', '05136462233'], ['Büsra Sert', '05221115568'], ['Öznur Hakkı', '05125468800'],
		 ['Mehmet Dal', '06771224567'], ['Melike Aynur', '05216750076'], ['Uğur Kaplan', '05235467733']]

# Q6 rehber.txt adındaki dosyayı okuyun. Daha sonra kullanıcıdan bir isim soyisim alın ve ona ait olan numarayı
# ekrana yazdırın. Eğer o kişi rehberde yoksa böyle bir numara yoktur diye kullanıcıyı uyarın

# Q7 bir program yazın ilk başta iki seçenek olsun. birincisi rehbere numara ekleme ikincisi de rehberde bulunan
# birinin numarasini öğrenme yani 6 daki soru. Eğer kullanıcı birinci seçeneği seçerse, iki tane input al birincisi
# isim soyisim, diğeri numara ve bunu rehbere kaydet. ikinci seçeneği seçerse, 6. sorudaki işi yapsın