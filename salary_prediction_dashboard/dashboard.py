
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Judul dan Deskripsi
st.title('Dashboard Job Analytics')
st.write('Dashboard Intractive Job Analytics')

# 2. Load Data
# (Pastikan nama file CSV-nya sesuai dengan yang ada di folder Anda)
df = pd.read_csv('job_salary_prediction_dataset.csv')

# 3. Membuat Filter Interaktif
st.sidebar.header('Pengaturan Panel')
# Mengambil semua daftar pekerjaan yang unik dari data
daftar_pekerjaan = df['job_title'].unique()
# Membuat tombol dropdown di menu samping (sidebar)
pilihan_profesi = st.sidebar.selectbox('Pilih Profesi untuk Dianalisis:', daftar_pekerjaan)

# Memfilter data sesuai dengan pilihan pengguna di dropdown
df_filtered = df[df['job_title'] == pilihan_profesi]




# 4. Menampilkan tabel sekilas
st.subheader(f'Prieview Data: {pilihan_profesi}')
st.dataframe(df_filtered.head())

# 5. Visualisasi 1: Tren Gaji vs Pengalaman (Line Chart)
st.subheader('Experience effect on Salary')
tren_gaji = df_filtered.groupby('experience_years')['salary'].mean()
st.line_chart(tren_gaji)


# 6. Visualisasi 2: Dampak Sertifikasi (Bar Chart)
st.subheader('Certification effect on Salary')
sertifikasi_gaji = df_filtered.groupby('certifications')['salary'].mean()
st.bar_chart(sertifikasi_gaji)

# Tambahkan ini di bagian bawah untuk memunculkan peta
st.subheader('Rate Salary Value Country')
# Menghitung rata-rata gaji per negara lalu merapikan formatnya
gaji_lokasi = df_filtered.groupby('location')['salary'].mean().reset_index()

# Membuat peta interaktif dengan Plotly
fig = px.choropleth(gaji_lokasi,
                    locations='location',
                    locationmode='country names',
                    color='salary',
                    hover_name='location',
                    color_continuous_scale='Viridis',
                    title='Persebaran jenis pekerjaan berdasarkan lokasi')

# Menampilkan grafik plotly di Streamlit
st.plotly_chart(fig)

# 7. Visualisasi 3: Efek Sistem Kerja (Remote Work)
st.subheader('Remote Work vs WFO')


# Menghitung rata-rata gaji berdasarkan sistem kerja
gaji_remote = df_filtered.groupby('remote_work')['salary'].mean().reset_index()

# Membuat Bar Chart interaktif dengan Plotly
fig_remote = px.bar(gaji_remote,
                    x='remote_work',
                    y='salary',
                    color='remote_work', # Memberikan warna berbeda untuk tiap sistem kerja
                    title='Rata-rata Gaji Berdasarkan Lokasi Kerja')

# Menampilkan grafiknya ke dalam dashboard
st.plotly_chart(fig_remote)





# 7. Visualisasi 3: Komposisi Sistem Kerja (Pie Chart)
st.subheader('JOB Remote Hybrid And On Site')

# Menghitung jumlah orang untuk masing-masing kategori sistem kerja
komposisi_remote = df_filtered['remote_work'].value_counts().reset_index()

# Merapikan nama kolom agar mudah dibaca oleh Plotly
komposisi_remote.columns = ['Sistem_Kerja', 'Jumlah_Pekerja']

# Membuat Pie Chart interaktif dengan Plotly
fig_pie = px.pie(komposisi_remote,
                 names='Sistem_Kerja',
                 values='Jumlah_Pekerja',
                 title='Persentase Karyawan Remote vs Hybrid vs On-site',
                 hole=0.4) # Trik rahasia: 'hole' mengubah Pie Chart menjadi Donut Chart yang lebih modern!

# Menampilkan grafiknya ke dalam dashboard
st.plotly_chart(fig_pie)








#company rate
company_rate = df_filtered.groupby('company_size')['salary'].mean().reset_index()

st.subheader('Company rate: startup vs enterprise')

# 2. Membuat Grafik Batang (Bar Chart) yang rapi
fig_perusahaan = px.bar(company_rate,
                        x='company_size', # Sumbu mendatar (kategori)
                        y='salary',       # Sumbu tegak (angka gaji)
                        color='company_size', # Biar warnanya beda-beda
                        title='Average Salary by Company Size')

# 3. Menampilkan ke Dashboard
st.plotly_chart(fig_perusahaan)

