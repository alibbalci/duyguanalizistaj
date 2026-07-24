import joblib
import streamlit as st

model = joblib.load(
    "models/logistic_regression_model.pkl"
)

tfidf = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

etiket_isimleri = {
    0: "Negatif",
    1: "Nötr",
    2: "Pozitif"
}

st.title("Türkçe Metin Duygu Analizi")

metin = st.text_area(
    "Analiz edilecek metni giriniz:"
)

if st.button("Duyguyu Analiz Et"):
    if not metin.strip():
        st.warning(
            "Lütfen bir metin giriniz."
        )
    else:
        metin_tfidf = tfidf.transform(
            [metin]
        )

        tahmin = model.predict(
            metin_tfidf
        )[0]

        st.success(
            f"Tahmin: {etiket_isimleri[tahmin]}"
        )