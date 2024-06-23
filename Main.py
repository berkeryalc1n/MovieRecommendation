import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Enter the path of the folder where you downloaded the files

# Dosyaları indirdiğiniz klasörün yolunu gir
credits = pd.read_csv("G:/My Drive/tez/veri seti/tmdb5000/credits.csv")
movies = pd.read_csv("G:/My Drive/tez/veri seti/tmdb5000/movies.csv")

# Make the name of the id variable in credits the same as the other file. combine data. Then combine the data sets by id and title using the merge method

# credits'deki id değişkeninin adını diger dosya ile aynı yapy. verileri birleştir. ardından veri setlerini merge metodunu kullanarak id ve title üstünden birleştir
credits = credits.rename(columns={"movie_id": "id"})
df_merge = pd.merge(credits, movies, left_on=['title','id'], right_on=['title','id'])

# Use TfidfVectorizer to create TF-IDF vectors and create TF-IDF matrix using Overview column

# TF-IDF vektörlerini oluşturmak için TfidfVectorizer'ı kullan ve Overview sütununu kullanarak TF-IDF matrisini oluştur
tfidf_vectorizer = TfidfVectorizer()
overview_tfidf_matrix = tfidf_vectorizer.fit_transform(df_merge["overview"].values.astype('U'))

# Get the name of the movie to be recommended. Find the relevant movie.

# Öneri yapılacak filmin adını alın. İlgili filmi bulun.
film_adi = input("Enter Movie Name: ")
film = df_merge[df_merge["title"] == film_adi]

if film.empty:
    # If the movie is not found, print an error message.
    
    # Eğer film bulunamadı ise hata mesajı yazdır.
    print("The selected movie was not found.")
else:
    # Create the TF-IDF vector for the corresponding movie
    # Calculate cosine similarity scores between movies
    # Sort movies other than the relevant movie according to their similarity scores and get the top five
    # Print suggestions to the screen
    # Print Movie Type
    
    # İlgili film için TF-IDF vektörünü oluşturun
    # Filmler arasındaki kozine benzerlik skorlarını hesaplayın
    # İlgili film dışındaki filmleri benzerlik skorlarına göre sıralayın ve ilk beşini alın
    # Önerileri ekrana yazdırın
    # Film Türünü yazdırın

    film_turu = film["genres"].values[0]
    film_tfidf = tfidf_vectorizer.transform(film["overview"].values.astype('U'))
    benzerlik_skorlari = cosine_similarity(film_tfidf, overview_tfidf_matrix)
    oneriler = df_merge.iloc[np.argsort(benzerlik_skorlari[0])[-6:-1]][::-1]

    print("The selected movie: ",film_adi)
    film_turu_str = ", ".join([genre["name"] for genre in eval(film_turu)])
    print("Movie Genre:", film_turu_str,"\n")
    print("Similar Movies:")
    print(oneriler["title"])

