# Yapay Zeka Destekli Kod Üretici

Bu proje, kullanıcıdan alınan prompt (istek) ile yapay zekâ destekli Python kodu üreten bir web uygulamasıdır. Kullanıcıdan alınan istek doğrultusunda, yapay zeka modeli (Ollama) tarafından
üretilen Python kodu web arayüzünde gösterilir.

## Kullanılan Teknolojiler

 1. **Ollama (Yapay Zeka Modeli)**
Projede, **Ollama** adlı yapay zeka modeli kullanılarak kullanıcıdan alınan promptlara göre Python kodu üretilmiştir.

Ollama modeli, yerel ortamda çalıştırılabilir ve düşük maliyetli altyapı gereksinimleriyle hızlı sonuçlar verir. Bu, projeyi daha verimli ve erişilebilir kılar.

 2. **Docker**
*Docker uygulamanın taşınabilirliğini ve izole edilmesini sağlamak amacıyla kullanılmıştır.
Flask uygulaması, Docker container'ı içinde çalıştırılmıştır. Bu sayede, Flask uygulamasının bağımlılıkları ve yapılandırmaları, herhangi bir ortamda doğru şekilde çalışacak şekilde paketlenmiştir.

3. Kubernetes ve Minikube
Kubernetes, modern mikro hizmet mimarileri için bir container orkestrasyon platformudur. Bu proje için Minikube kullanarak Kubernetes'in yerel bir sürümünü çalıştırdık.
Minikube, Kubernetes'i bir sanal makine üzerinde çalıştırarak uygulamaların kolayca dağıtılmasını ve yönetilmesini sağlar.

Kubernetes Yapılandırması:
Deployment.yaml ve service.yaml dosyaları ile Flask uygulaması, Kubernetes pod'ları olarak dağıtıldı.
NodePort servisi ile dış dünyaya açılan bir port üzerinden erişim sağlandı.

Flask Kullanımı:
HTML Formu aracılığıyla kullanıcıdan bir prompt alınır.
Kullanıcıdan alınan prompt ile Ollama modeline istek gönderilir ve üretilen Python kodu kullanıcıya sunulur.

Minikube Dağıtımı
Minikube kullanılarak yerel ortamda Kubernetes pod'ları çalıştırıldı ve Flask uygulaması Kubernetes ortamında dağıtıldı


Mert Tosun - tosun8770@gmail.com

