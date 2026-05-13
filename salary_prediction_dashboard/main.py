import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('job_salary_prediction_dataset.csv')

#mencari tahu gaji rata rata seseorang melalui tingkatan pendidikan
education_salary_level = df.groupby('education_level')['salary'].mean().sort_values(ascending=False)

#memfilter job tittle untuk profesi data analis
df_data_analyst = df[df['job_title'] == 'Data Analyst']

#melihat gaji rata  rata data analyst
tren_gaji = df_data_analyst.groupby('experience_years')['salary'].mean().sort_values(ascending=False)

#melihat gaji berdasarkan sertifikasi
certification_salary = df_data_analyst.groupby('certifications')['salary'].mean().sort_values(ascending=False)


#menampilkan data gaji dari tingkatan pendidikan
#print(education_salary_level)

#melihat info pada data
print(df.info())

#melihat filter job data analyst
#print(df_data_analyst)

#melihat tren gaji
#print(tren_gaji)

#line chart tren gaji
#tren_gaji.plot(kind='line', marker='o', color='blue')

#bar salary berdasarkan tingkat pendidikan
#education_salary_level.plot(kind='bar', color='coral')
#plt.title('Rata-rata Gaji Berdasarkan Tingkat Pendidikan')
#plt.ylabel('Rata-rata Gaji')
#plt.xlabel('Tingkat Pendidikan')



#membuat bar gaji berdasarkan sertifikasi
certification_salary.plot(kind='bar', color='coral')

plt.show()