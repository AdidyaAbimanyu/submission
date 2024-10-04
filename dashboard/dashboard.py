import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv('./data/day.csv')

# Pertanyaan 1
filter_holiday = day_df[(day_df['weekday'] >= 1) & (day_df['weekday'] <= 6) & (day_df['holiday'] == 1)]
average_sales_holiday = filter_holiday['cnt'].mean()

filter_weekday = day_df[(day_df['weekday'] >= 1) & (day_df['weekday'] <= 6) & (day_df['holiday'] == 0)]
average_sales_weekday = filter_weekday['cnt'].mean()
data_q1 = {
    'Jenis Hari': ['Weekday', 'Holiday'],
    'Rata-rata Peminjaman Per Hari': [round(average_sales_weekday, 2), average_sales_holiday]
}
visualization_df_q1 = pd.DataFrame(data_q1)

# Pertanyaan 2
average_sales_casual = day_df['casual'].mean()
avarage_sales_registered = day_df['registered'].mean()
data_q2 = {
    'Jenis Orang': ['Casual', 'Registered'],
    'Rata-rata Peminjaman Per Hari': [round(average_sales_casual, 2), round(avarage_sales_registered, 2)]
}
visualization_df_q2 = pd.DataFrame(data_q2)

# Streamlit
st.title('Dashboard Peminjaman Sepeda')
st.write('**Menganalisa dataset Bike Sharing**')
st.caption('Source: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset')

st.write('### Pertanyaan 1')
st.write('**Bagaimana rata-rata peminjaman sepeda berdasarkan hari biasa (weekday) dan hari libur (holiday)? manakah yang lebih tinggi?**')
st.write('### Pertanyaan 2')
st.write('**Bagaimana rata-rata peminjaman sepeda berdasarkan orang yang tidak memiliki keanggotaan (casual) dan yang memiliki keanggotaan (registered)? manakah yang lebih tinggi?**')

with st.expander('Analisis pertanyaan 1'):
    st.subheader('Rata-rata Peminjaman Sepeda Berdasarkan Jenis Hari')
    st.write(visualization_df_q1)
    
    # Visualisasi
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Jenis Hari', y='Rata-rata Peminjaman Per Hari', data=visualization_df_q1, palette='viridis', hue='Jenis Hari', dodge=False, legend=True)
    plt.title('Perbandingan Rata-rata Peminjaman Sepeda')
    plt.ylabel('Rata-rata Peminjaman Per Hari')
    plt.xlabel('Jenis Hari')
    plt.ylim(0, max(visualization_df_q1['Rata-rata Peminjaman Per Hari']) * 1.1)
    st.pyplot(plt)
    
with st.expander('Analisis pertanyaan 2'):
    st.subheader('Rata-rata Peminjaman Sepeda Berdasarkan Jenis Orang')
    st.write(visualization_df_q2)
    
    # Visualisasi
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Jenis Orang', y='Rata-rata Peminjaman Per Hari', data=visualization_df_q2, palette='viridis', hue='Jenis Orang', dodge=False, legend=True)
    plt.title('Perbandingan Rata-rata Peminjaman Sepeda')
    plt.ylabel('Rata-rata Peminjaman Per Hari')
    plt.xlabel('Jenis Orang')
    plt.ylim(0, max(visualization_df_q2['Rata-rata Peminjaman Per Hari']) * 1.1)
    st.pyplot(plt)
    
# Kesimpulan
st.write('### Kesimpulan')
st.write('1. Kesimpulan dari pertanyaan pertama adalah rata-rata peminjaman sepeda berdasarkan hari biasa (weekday) lebih tinggi sedikit daripada hari libur (holiday). Ini merupakan suatu hal yang tidak terduga karena hari libur (holiday) jumlahnya sangat sedikit dibandingan hari biasa (weekday).')
st.write('2. Kemudian kesimpulan kedua adalah rata-rata peminjaman sepeda berdasarkan orang yang memiliki keanggotaan (registered) lebih tinggi daripada yang tidak memiliki keanggotaan (casual).')

# Copyright
st.caption('Copyright @ Adidya Abimanyu')