import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# verileri yüklüyoruz
credits = pd.read_csv("G:/My Drive/tez/veri seti/tmdb5000/credits.csv")
movies = pd.read_csv("G:/My Drive/tez/veri seti/tmdb5000/movies.csv")

# verilere göz atıyoruz
#print("1 :", credits.info(),"\n")
#print("2 :", movies.info(),"\n")

# credits'deki id değişkeninin adını diger dosya ile aynı yapyıyoruz. verileri birleştiriyoruz. ardından veri setlerini merge metodunu kullanarak id ve title üstünden
# birleştiriyoruz..
credits = credits.rename(columns={"movie_id": "id"})
df_merge = pd.merge(credits, movies, left_on=['title','id'], right_on=['title','id'])


# TF-IDF vektörlerini oluşturmak için TfidfVectorizer'ı kullanın
# Overview sütununu kullanarak TF-IDF matrisini oluşturun

tfidf_vectorizer = TfidfVectorizer()
overview_tfidf_matrix = tfidf_vectorizer.fit_transform(df_merge["overview"].values.astype('U'))


# Öneri yapılacak filmin adını alın. İlgili filmi bulun

film_adi = input("Enter Movie Name: ")
film = df_merge[df_merge["title"] == film_adi]

# Eğer film bulunamadı ise hata mesajı yazdır. İlgili filmin türünü alın
if film.empty:
    print("The selected movie was not found.")
else:
    film_turu = film["genres"].values[0]
    film_tfidf = tfidf_vectorizer.transform(film["overview"].values.astype('U'))
    benzerlik_skorlari = cosine_similarity(film_tfidf, overview_tfidf_matrix)
    oneriler = df_merge.iloc[np.argsort(benzerlik_skorlari[0])[-6:-1]][::-1]

    print("The selected movie: ",film_adi)
    film_turu_str = ", ".join([genre["name"] for genre in eval(film_turu)])
    print("Movie Genre:", film_turu_str,"\n")
    print("Similar Movies:")
    print(oneriler["title"])

    # İlgili film için TF-IDF vektörünü oluşturun
    # Filmler arasındaki kozine benzerlik skorlarını hesaplayın
    # İlgili film dışındaki filmleri benzerlik skorlarına göre sıralayın ve ilk beşini alın
    # Önerileri ekrana yazdırın
    # Film Türünü yazdırın
