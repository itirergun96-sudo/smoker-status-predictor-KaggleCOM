---
title: Smoker Status Prediction
emoji: 🚬
colorFrom: indigo
colorTo: green
sdk: streamlit
sdk_version: 1.30.0
app_file: src/app.py
pinned: false
---

# 🚬 Binary Prediction of Smoker Status using Bio-Signals

Bu proje biyometrik sağlık verilerinden sigara kullanım durumunu tahmin eden uçtan uca bir makine öğrenmesi çalışmasıdır. Kaggle Playground yarışması kapsamında geliştirilmiş olup veri analizi, model eğitimi ve deploy adımlarını içeren tekrar üretilebilir bir pipeline sunar.

---

## 🎯 Amaç

Biyolojik sinyaller üzerinden bireylerin sigara kullanma durumunu tahmin eden bir sınıflandırma modeli geliştirmek ve sağlık analitiği için veri temelli bir yaklaşım oluşturmak.

---

## 📊 Veri Seti

Veri seti bireylerin yaş, boy, kilo, kan değerleri ve çeşitli biyometrik ölçümlerini içerir. Her satır bir kişiyi temsil eder ve hedef değişken:

**smoking → sigara kullanım durumu (binary)**

---

## 🧠 Model

Baseline model: **Random Forest Classifier**

Model:

- sayısal verilerle stabil çalışır
- hızlı eğitilir
- güçlü bir referans baseline sağlar

---

## ⚙️ Pipeline

1. Data Loading  
2. Exploratory Data Analysis  
3. Feature Engineering  
4. Model Training  
5. Validation  
6. Submission Generation  
7. Model Saving  

---

## Demo

https://huggingface.co/spaces/abmias/smoker-statur-predictor-KaggleCOM


