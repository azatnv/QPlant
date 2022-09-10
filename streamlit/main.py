import streamlit as st
import pandas as pd
import numpy as np
import requests
import re

number_chromosomes = {
    "Cucumis sativus" : 7,
    "Zea mays": 10,
    "Triticum aestivum" : 7
}
crops = ("Cucumis sativus", "Zea mays", "Triticum aestivum")

# backend_url = "http://localhost:8502/upload"
backend_url = "http://fastapi:8502/upload"

def upload(url: str, crop: str, region: str, file):
    files = {"vcf": ("name.vcf.gz", file, 'text/plain')}
    with st.spinner('Пожалуйста подождите...'):
        response = requests.post(
            url=backend_url,
            data={"crop": crop, "region": region},
            files=files)
        with open(f"QPlant.out.vcf.gz", 'wb') as output_file:
            output_file.write(response.content)
        st.success('Готово!')

    print(f"Пришло {len(response.content)}")

current_crop = st.sidebar.selectbox(
    "Выберите культуру", crops
)
st.title(f"Вставка пропусков в геном \"{current_crop}\"")

with st.form("upload_vcf"):
    uploaded_file = None
    
    st.header("Шаг 1. Выберите файл VCF")
    st.write("""
        На этом этапе пользователи могут загрузить файл VCF
        или ввести текст для импутации негенотипированных маркеров.
        """)

    vcf_file = st.file_uploader("Выберите файл VCF", type=[".vcf.gz"])
    if vcf_file is not None:
        uploaded_file = vcf_file.getvalue()

    container1 = st.container()
    container1.header("Шаг 2. Выберите регион хромосомы")
    container1.write("""
        Пользователям необходимо ввести область 
        хромосомы для выполнения импутации.""")
    region = container1.text_input('Регион', placeholder='Chr1:1-1000000')

    container2 = st.container()
    container2.header("""Шаг 3. Отправьте и скачайте результаты""")
    container2.write("""Нажмите кнопку “Отправить”, чтобы выполнить 
        импутацию. Вычисление может занять 3 минуты.
        Результаты будут скачаны в формате VCF.""")

    submitted_vcf = st.form_submit_button("Отправить")
    if submitted_vcf and (vcf_file is not None
        and re.match(f'^Chr[1-{number_chromosomes[current_crop]}]:\d-\d+$', region)):
        upload(backend_url, current_crop, region, uploaded_file)
        print(f"Ушло {len(uploaded_file)}")


st.download_button(
    label='Скачать результат',
    data=open(f"QPlant.out.vcf.gz", "rb"),  
    file_name="QPlant.out.vcf.gz"
)