"""
Burası Yorum satırıdır 

Buradaki her bir sorunun çözümünü ayrı bir .py dosyasının içine koyarak, bu dosyaları 
1.week klasörüne koyup githuba yükleyin.
"""

# Q1 Ilk önce benim yolladığım kodu yani 'hello_world.py' dosyasını çalıştırın


# Q2. Ekranda
"""
Hello World
How are you
"""
# yazmasını bekliyorum, fakat bunu yaparken bir tane print kullanın

# Q3 Bu iki değişkenin toplamını fakını çarpımını bölümünü ve modunu ekrana yazdırın
number_1 = 34
number_2 = 128

# Q4 Bu iki değişkeni integer yapıp bir arrayin içine atıp onu ekrana yazdırın
number_1 = '324'
number_2 = "183"

# Q5 Bu iki arraydeki stringleri kendi içinde birleştirip birer integer haline getirin, ve daha sonra çarpıp
# çarpıp kareköknü ekrana yazdırın ve ayrıca eşitliğini kontrol edip onu da ekrar yazdırın
array_1 = ['5', '2', '8']
array_2 = ['7', '0', '1']

# Q6 Bu iki textin eşitliğini konrtol edin ekrana yazdırın, Daha sonra eşit olacak şekilde gerekli
# fonksiyonlardan geçirin. Textlere herhangi bir ekleme çıkarma yapmadan eşit hale getirin.
text_1 = 'ThIs is TexT'
text_2 = 'This iS TExt'

# Q7 Bu arraydeki isim ve soyismi ters çevirip ekrana yazdırın
array = ['Ahmet', 'Yılmaz']
# Yılmaz Ahmet olmalı yani

# Q8 İki testteki yazıları silip textte sadece numaralar kalmalı ve daha sonra bu numaraları birleştirip toplayın
text_1 = "Bu cümlede 4 elma 5 armut 8 tane de muz var"
text_2 = 'bu ikinci cümlede 9 kiraz 3 karpuz var'

# cevabın 458 + 93 = 551 olması gerek bunu ekrana yazdırın

# Q7 Bu textteki yazı hariç herşeyi kaldırın. Textte sadece alfabetik harfler kalsın
text = """
As described previously, the captured views provide us two important data: 1) 
silhouettes of the object from different views, which define the visual hull of the object, and 
2) ray-ray correspondences before and after rays intersecting with the object, which correlate to light 
refraction paths and surface geometry details.
"""
# sonuç alttaki gibi olsun

"""
As described previously the captured views provide us two important data
silhouettes of the object from different views which define the visual hull of the object and 
ray-ray correspondences before and after rays intersecting with the object which correlate to light 
refraction paths and surface geometry details
"""

# Q8 Bu textte geçen toplam kelime sayısını bulmanızı istiyorum
text = """
Here we first explain the setup that we have designed for data acquisition. As shown in Fig. 2, 
the transparent object to be captured is placed on Turntable #1. Two cameras are used and both are fixed during 
the capture process. Camera #1 is positioned in front of the transparent object and Camera #2 above it. 
Both cameras have their intrinsic parameters and relative positions calibrated [Zhang 2000]. In addition, 
through putting a checkerboard pattern on the turntable, its rotation axis with respect to the two cameras is also 
calibrated. Similar to the previous work [Qian et al. 2016], a monitor is used as light source. Nonetheless, 
instead of manually moving the monitor during acquisition to capture starting locations and orientations of 
incoming rays, we place the monitor on top of Turntable #2. The monitor’s position can then be precisely and 
automatically adjusted. To start the acquisition, we use Turntable #2 to set the monitor at its first position, 
which is calibrated with the cameras through displaying a checkerboard pattern. At this monitor position, we rotate
the transparent target object using Turntable #1 to observe it from a set of (8 by default) directions that 
evenly sample the 360o viewing angle. At each direction, a series of binary Gray codes are displayed for both 
silhouette extraction [Zongker et al. 1999] and environment matting. The latter allows us to determine the pixel 
location on monitor that corresponds to a given ray refracted by the object and observed by Camera #1.
"""
# Burada geçen toplam geçen kelime sayısını ekrana yazdırın.

# Q9 Yukarıdaki en çok geçen kelimeyi ve sayısını ekrana yazdırın. "pattern." ile "pattern" aynı kelime olarak sayılmalı
