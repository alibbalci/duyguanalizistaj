
# Türkçe Metin Duygu Analizi Sistemi

Bu proje, kullanıcı tarafından girilen Türkçe metinleri **Pozitif**, **Negatif** veya **Nötr** olarak sınıflandıran bir doğal dil işleme uygulamasıdır.

Proje, yapay zeka stajı kapsamında NLP, veri ön işleme, makine öğrenmesi, model karşılaştırma, arayüz geliştirme ve teknik raporlama konularında uçtan uca deneyim kazanmak amacıyla geliştirilmektedir.

---

## Projenin Amacı

Bu projenin temel amacı, Türkçe metinler üzerinde duygu analizi gerçekleştirerek kullanıcının yazdığı bir metnin hangi duygu sınıfına ait olduğunu tahmin eden bir sistem geliştirmektir.

Proje kapsamında:

- NLP temel kavramlarının öğrenilmesi
- Türkçe metin verilerinin analiz edilmesi
- Veri temizleme ve ön işleme işlemlerinin uygulanması
- Metinlerin sayısal verilere dönüştürülmesi
- Farklı makine öğrenmesi modellerinin eğitilmesi
- Modellerin performanslarının karşılaştırılması
- Kullanıcı arayüzü geliştirilmesi
- Teknik rapor ve sunum hazırlanması

hedeflenmektedir.

---

## Proje Tanımı

Sistem, kullanıcı tarafından girilen Türkçe bir metni analiz ederek aşağıdaki sınıflardan birine ait olduğunu tahmin eder:

- **Pozitif**
- **Negatif**
- **Nötr**

Örnek:

```text
Girdi: Ürün gerçekten çok güzel ve kaliteli.
Tahmin: Pozitif
```

```text
Girdi: Siparişim çok geç geldi ve ürün hasarlıydı.
Tahmin: Negatif
```

```text
Girdi: Ürün bugün teslim edildi.
Tahmin: Nötr
```

---

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- NLTK veya benzeri NLP kütüphaneleri
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit veya Gradio
- Joblib
- Jupyter Notebook

---

## Kullanılacak Makine Öğrenmesi Modelleri

Projede birden fazla makine öğrenmesi modeli eğitilecek ve sonuçları karşılaştırılacaktır.

### Multinomial Naive Bayes

Metin sınıflandırma problemlerinde sık kullanılan, hızlı ve temel bir sınıflandırma modelidir.

### Logistic Regression

Metin verileri üzerinde başarılı sonuçlar verebilen doğrusal bir sınıflandırma algoritmasıdır.

### Support Vector Machine

Sınıflar arasındaki en uygun karar sınırını belirlemeye çalışan ve metin sınıflandırmada sık kullanılan bir algoritmadır.

---

## Metin İşleme Süreci

Sistemde metinler doğrudan makine öğrenmesi modeline verilmez. Öncelikle aşağıdaki işlemler uygulanır:

1. Metnin küçük harfe dönüştürülmesi
2. URL adreslerinin kaldırılması
3. Kullanıcı etiketlerinin kaldırılması
4. Gereksiz noktalama işaretlerinin temizlenmesi
5. Sayıların temizlenmesi veya anlamlı şekilde işlenmesi
6. Fazla boşlukların kaldırılması
7. Stop word temizliği
8. Gerektiğinde stemming veya lemmatization uygulanması
9. Metinlerin TF-IDF ile sayısal verilere dönüştürülmesi

Genel işlem akışı:

```text
Ham Metin
   ↓
Veri Temizleme
   ↓
Metin Ön İşleme
   ↓
TF-IDF Vektörleştirme
   ↓
Makine Öğrenmesi Modeli
   ↓
Pozitif / Negatif / Nötr Tahmini
```

---

## TF-IDF

Makine öğrenmesi modelleri doğrudan metinleri anlayamaz. Bu nedenle metinler TF-IDF yöntemi kullanılarak sayısal vektörlere dönüştürülür.

TF-IDF, bir kelimenin belirli bir metin içerisindeki önemini hesaplar.

Örneğin:

```text
Ürün çok güzel ve kaliteli.
```

cümlesindeki kelimeler TF-IDF sonucunda sayısal değerlere dönüştürülür. Model, bu sayısal değerleri kullanarak duygu sınıfını öğrenir.

---

## Veri Seti

Projede Türkçe ve etiketli bir duygu analizi veri seti kullanılacaktır.

Veri setinin en az aşağıdaki sütunları içermesi beklenmektedir:

| Sütun | Açıklama |
|---|---|
| `text` | Kullanıcı yorumu veya Türkçe metin |
| `label` | Metnin duygu etiketi |

Örnek veri:

| text | label |
|---|---|
| Ürün çok güzel, çok memnun kaldım. | positive |
| Kargo çok geç geldi. | negative |
| Ürün bugün teslim edildi. | neutral |

Veri seti seçilirken aşağıdaki kriterler değerlendirilecektir:

- Türkçe metinlerden oluşması
- Etiketlerin güvenilir olması
- Pozitif, negatif ve nötr sınıflarını içermesi
- Sınıf dağılımının dengeli olması
- Eksik ve tekrarlanan verilerin az olması
- Veri sayısının model eğitimi için yeterli olması
- Kaynağın ve lisans bilgisinin belirtilmiş olması

---

## Proje Aşamaları

### 1. Hafta — Literatür Araştırması ve Veri Seti Analizi

- NLP kavramlarının araştırılması
- Duygu analizinin çalışma mantığının öğrenilmesi
- Metin sınıflandırma yöntemlerinin incelenmesi
- Türkçe veri setlerinin araştırılması
- Veri setinin seçilmesi
- Veri setinin sütun ve sınıf dağılımlarının analiz edilmesi
- Araştırma dokümanının hazırlanması

### 2. Hafta — Veri Temizleme ve İlk Modeller

- Eksik verilerin kontrol edilmesi
- Tekrarlanan kayıtların temizlenmesi
- Metin temizleme fonksiyonlarının hazırlanması
- Verinin eğitim ve test olarak ayrılması
- TF-IDF uygulanması
- İlk makine öğrenmesi modelinin eğitilmesi
- İlk tahmin sonuçlarının alınması

### 3. Hafta — Model Eğitimi ve Karşılaştırma

- Naive Bayes modelinin eğitilmesi
- Logistic Regression modelinin eğitilmesi
- SVM modelinin eğitilmesi
- Modellerin aynı test verisi üzerinde değerlendirilmesi
- Accuracy, precision, recall ve F1-score değerlerinin hesaplanması
- Confusion matrix oluşturulması
- En başarılı modelin seçilmesi
- Model karşılaştırma raporunun hazırlanması

### 4. Hafta — Arayüz ve Final Teslimi

- Streamlit veya Gradio arayüzünün geliştirilmesi
- Eğitilmiş modelin arayüze bağlanması
- Kullanıcıdan metin alınması
- Tahmin sonucunun ekranda gösterilmesi
- Proje testlerinin yapılması
- README dosyasının tamamlanması
- Teknik raporun hazırlanması
- Sunum ve demo hazırlığının yapılması

---

## Model Değerlendirme Metrikleri

Modeller aşağıdaki metriklere göre karşılaştırılacaktır:

### Accuracy

Modelin yaptığı toplam tahminlerin ne kadarının doğru olduğunu gösterir.

### Precision

Modelin belirli bir sınıfa ait olarak tahmin ettiği örneklerin ne kadarının gerçekten o sınıfa ait olduğunu gösterir.

### Recall

Gerçekte belirli bir sınıfa ait olan örneklerin ne kadarının model tarafından doğru bulunduğunu gösterir.

### F1-Score

Precision ve recall değerlerinin dengeli ortalamasıdır.

Özellikle veri setindeki sınıflar dengesiz olduğunda yalnızca accuracy değerine bakmak yeterli değildir. Bu nedenle macro F1-score sonucu da dikkate alınacaktır.

---

## Eğitim ve Test Verisi

Veri seti eğitim ve test verisi olmak üzere ikiye ayrılacaktır.

Örnek dağılım:

```text
%80 Eğitim Verisi
%20 Test Verisi
```

- Eğitim verisi modelin öğrenmesi için kullanılır.
- Test verisi modelin daha önce görmediği metinler üzerindeki başarısını ölçmek için kullanılır.

Sınıf dağılımını korumak için `stratify` parametresi kullanılacaktır.

---

## Önerilen Proje Yapısı

```text
turkce-duygu-analizi/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── dataset.csv
│   └── processed/
│       └── cleaned_dataset.csv
│
├── notebooks/
│   ├── 01_veri_analizi.ipynb
│   ├── 02_veri_temizleme.ipynb
│   └── 03_model_karsilastirma.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
│   ├── sentiment_model.joblib
│   └── tfidf_vectorizer.joblib
│
├── reports/
│   ├── teknik_rapor.pdf
│   └── figures/
│       ├── class_distribution.png
│       └── confusion_matrix.png
│
└── presentation/
    └── proje_sunumu.pptx
```

---

## Kurulum

Projeyi bilgisayarınıza indirin:

```bash
git clone REPO_ADRESI
cd turkce-duygu-analizi
```

Sanal ortam oluşturun:

```bash
python -m venv venv
```

Windows için sanal ortamı etkinleştirin:

```bash
venv\Scripts\activate
```

macOS ve Linux için:

```bash
source venv/bin/activate
```

Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

---

## Örnek requirements.txt

```text
pandas
numpy
scikit-learn
nltk
matplotlib
seaborn
streamlit
joblib
jupyter
```

Gradio kullanılacaksa:

```text
gradio
```

paketi de eklenmelidir.

---

## Model Eğitimi

Modeli eğitmek için:

```bash
python src/train.py
```

Eğitim işlemi tamamlandığında model ve TF-IDF nesnesi `models` klasörüne kaydedilecektir.

Örnek:

```text
models/sentiment_model.joblib
models/tfidf_vectorizer.joblib
```

---

## Uygulamayı Çalıştırma

Streamlit kullanılıyorsa:

```bash
streamlit run app.py
```

Gradio kullanılıyorsa:

```bash
python app.py
```

Uygulama çalıştırıldıktan sonra kullanıcı metin kutusuna Türkçe bir metin girer ve sistem aşağıdaki sonuçlardan birini gösterir:

```text
Pozitif
Negatif
Nötr
```

---

## Örnek Kullanım

```python
from src.predict import predict_sentiment

text = "Bu ürünü çok beğendim, kesinlikle tavsiye ederim."
result = predict_sentiment(text)

print(result)
```

Örnek çıktı:

```text
Pozitif
```

---

## Model Karşılaştırma Tablosu

Model sonuçları eğitim tamamlandıktan sonra aşağıdaki tabloya eklenecektir:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Naive Bayes | - | - | - | - |
| Logistic Regression | - | - | - | - |
| SVM | - | - | - | - |

En başarılı model yalnızca accuracy değerine göre değil, precision, recall, F1-score ve confusion matrix sonuçları birlikte değerlendirilerek seçilecektir.

---

## Haftalık Teslimatlar

| Hafta | Teslim |
|---|---|
| 1. Hafta | Araştırma dokümanı ve veri seti seçimi |
| 2. Hafta | Veri temizleme işlemleri ve ilk model çıktıları |
| 3. Hafta | Model karşılaştırma raporu |
| 4. Hafta | Final proje, teknik rapor, sunum ve demo |

---

## Final Teslimleri

Proje sonunda aşağıdaki çalışmalar teslim edilecektir:

- GitHub repository
- Çalışan duygu analizi uygulaması
- Eğitilmiş makine öğrenmesi modeli
- Veri temizleme ve model eğitim kodları
- Model karşılaştırma sonuçları
- 5-10 sayfalık teknik rapor
- Proje sunumu
- Demo gösterimi

---

## Değerlendirme Kriterleri

| Kriter | Ağırlık |
|---|---:|
| Araştırma Kalitesi | %20 |
| Kod Kalitesi | %20 |
| Model Başarısı | %20 |
| Rapor Kalitesi | %20 |
| Sunum ve Anlatım | %20 |

---

## Kod Kalitesi İçin Dikkat Edilecek Noktalar

- Fonksiyon ve değişken isimleri anlamlı olmalıdır.
- Veri temizleme, eğitim, değerlendirme ve tahmin işlemleri farklı dosyalarda tutulmalıdır.
- Tekrarlanan kodlardan kaçınılmalıdır.
- Sabit dosya yolları yerine proje içi göreceli yollar kullanılmalıdır.
- Kod içerisinde gerekli açıklamalar bulunmalıdır.
- Model sonuçlarının tekrar üretilebilir olması için `random_state` kullanılmalıdır.
- Veri sızıntısını önlemek için TF-IDF yalnızca eğitim verisi üzerinde öğrenilmelidir.
- Model ve vektörleştirici birlikte kaydedilmelidir.

---

## Gelecekte Eklenebilecek Özellikler

- Tahmin güven oranının gösterilmesi
- Kullanıcı yorumlarının kaydedilmesi
- Yeni verilerle modelin yeniden eğitilmesi
- Derin öğrenme modellerinin denenmesi
- BERT tabanlı Türkçe modellerin kullanılması
- REST API geliştirilmesi
- Docker desteği
- Bulut ortamına deployment
- Toplu CSV dosyası analizi
- Duygu sonuçlarının grafiklerle gösterilmesi

---

## Proje Durumu

Proje geliştirme aşamasındadır.

- [X] Literatür araştırması
- [X] Veri seti seçimi
- [X] Veri seti analizi
- [X] Veri temizleme
- [ ] TF-IDF dönüşümü
- [ ] Naive Bayes modeli
- [ ] Logistic Regression modeli
- [ ] SVM modeli
- [ ] Model karşılaştırması
- [ ] Streamlit veya Gradio arayüzü
- [ ] Teknik rapor
- [ ] Sunum
- [ ] Final demo

---

## Geliştirici

**Ali Balcı**

Yazılım Mühendisliği Öğrencisi

---

## Lisans

Bu proje eğitim ve staj çalışması amacıyla geliştirilmiştir.

Kullanılan veri setinin lisans koşulları ayrıca kontrol edilmeli ve bu bölümde belirtilmelidir.
Kitaplık
/
README.md

