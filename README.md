# Drone-Programming
Auto Mission.py Dosyası bir txt dosyası içerisine yazılmış WayPoint'leri okuyarak AUTO modda Drone'un bu noktalara gitmesini sağlar.


Auto Waypoint.py Dosyası bir txt dosyası içerisinde değil, doğrudan program içerisine eklenmis Waypointlere AUTO modda Drone'un hareket etmesini sağlar.


Drone Blue Circle.py Dosyası kamera vasıtası ile tespit edilmiş Mavi dairenin üzerine Drone'un hareket etmesini sağlar. Mavi dairenin tam üstüne geldiğinde hareketi sonlanır.


Drone Red Circle.py Dosyası kamera vasıtası ile tespit edilmiş Kırmızı dairenin üzerinde Drone'un hareket Etmesini sağlar. Mavi dairenin tam üstüne geldiğinden hareketi sonlanır.


Simple Goto.py Dosyası Dronu'un çalışır duruma gelmesi, havalanması ve girilen koordinata hareket etmesini sağlar.



Burada Kırmızı daireyi tespit eden python kodunun nasıl çalıştığını görmektesiniz

https://github.com/siberkampus/Drone-Programming/assets/84104008/fb3cbc0c-2340-4204-8b91-1f0a1f1409df



Burada Mavi daireyi tespit eden python kodunun nasıl çalıştığını görmektesiniz.

https://github.com/siberkampus/Drone-Programming/assets/84104008/c928fafe-3e6a-44c9-852b-5836284375b8


Burada tespit ettiğimiz kırmızı dairenin üzerine drone'un konumlanmaya çalıştığını görmektesiniz. Drone kırmızı dairenin üzerinde konumlandığı zaman durmaktadır. Bu durumda kalkış iniş ya da görevler yapmayı deneyebilirsiniz. Kullanılan python kodu gazebo simülasyon programına entegre edilmiş ve dronun davranışları bu program içerisinde simülasyon edilmiştir.

https://github.com/siberkampus/Drone-Programming/assets/84104008/48240fd8-a37e-47e2-b219-12413a012fff

Ayrıca Ardupilot yer istasyonu programı ile haritadan belli koordinatlar seçerek drone'nun bu koordinatlara gitmesini sağlayabilirsiniz. Yani waypointler seçebilir ve bu waypointleri bir txt dosyasına ekleyerek kendi görev dosyanızı oluşturabilirsiniz.

2022 TEKNOFEST Yarışmasına hazırlanırken çalıştığım ekip arkadaşlarıma teşekkür ederim.
