# Movie Recommendation System with Python [EN]
The purpose of this project is to receive a movie input from the user, search for this movie in the dataset, and recommend similar movies. It is prepared with Python version 3.12.

## Setup
To run this project, you will need the following software and libraries:

-Python 3.12 or newer
-Other dependencies

### Step 1: Cloning the Project
Clone the project files to your local machine using the following command in your terminal:

"""bash
git clone https://github.com/berkeryalc1n/MovieRecommendation
cd Main.py

### Step 2: Creating the Virtual Environment
Create a virtual environment to manage dependencies:

"""bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate virtual environment (MacOS/Linux) or
.\venv\Scripts\activate  # Activate virtual environment (Windows)

pip install -r requirements.txt  # Install dependencies

### Step 3: Running the Application
To launch the application, execute the following command:

"""bash
python main.py

## Instructions
When we run the application, it asks us to enter a movie name. After entering the movie name, if the movie is in our dataset, it calculates the similarity of the movie summaries using the TF-IDF Vectorizer and recommends five similar movies. If the entered movie is not in the dataset, an error message is displayed and the application terminates.

# Movie Recommendation System with Python [TR]
Bu projenin amacı kullanıcıdan film girdisi alıp bu filmi veri setinde aratarak benzer filmler önermektir. Python 3.12 versiyonu ile hazırlanmıştır.

## Kurulum

Projenin çalışması için aşağıdaki yazılımlara ve kütüphanelere ihtiyaç vardır:
- Python 3.12 veya daha yeni bir sürüm
- Diğer gereksinimler

### Adım 1: Projenin İndirilmesi
Proje dosyalarını yerel makinenize klonlamak için terminalde şu komutu kullanın:

""" bash
git clone https://github.com/berkeryalc1n/MovieRecommendation
cd Main.py

### Adım 2: Sanal Ortamın Oluşturulması
Bağımlılıkları yönetmek için sanal bir ortam oluşturun:

"""bash
python -m venv venv  # Sanal ortam oluşturma
source venv/bin/activate  # Sanal ortamı etkinleştirme (MacOS/Linux) veya
.\venv\Scripts\activate  # Sanal ortamı etkinleştirme (Windows)

pip install -r requirements.txt  # Gereksinimlerin yüklenmesi

### Adım 3: Uygulamanın açılması
Uygulamayı başlatmak için aşağıdaki komutu yürütün:

"""bash
python main.py

## Kullanım Talimatları
[TR] Uygulamayı çalıştırdığımız zaman uygulama bizden bir film ismi girmemizi istiyor. Film ismini girdikten sonra eğer girilen film veri setimizde varsa TF-IDF Vectorizer kullanarak filmlerin özet bilgilerinin benzerliğini hesaplar ve benzer beş adet filmi önerir. Eğer girilen film veri setinde yoksa hata mesajı ekrana yazdırılır ve uygulama sonlanır.
[TR] 


