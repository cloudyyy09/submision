import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_day = pd.read_csv("bike_sharing_day.csv")
df_hour = pd.read_csv("bike_sharing_hour.csv")

# Mapping angka musim ke nama musim sebenarnya
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df_day["season"] = df_day["season"].map(season_mapping)

# 🎯 SETUP DASHBOARD
st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")

# 🎯 HEADER
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Menampilkan analisis data penyewaan sepeda berdasarkan musim, hari kerja, dan jam operasional.")

# 🎯 SIDEBAR - FILTER DATA
st.sidebar.header("🔍 Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", df_day['season'].unique())

# 📩 Informasi Kontak
st.sidebar.markdown("---")
st.sidebar.header("📩 Kontak")
st.sidebar.write("**Nama:** Revo Pratama")
st.sidebar.write("**ID Dicoding:** MC19D5Y1619")
st.sidebar.write("**Email:** revopratama2004@gmail.com")

# 🎯 FILTER DATA
filtered_df = df_day[df_day['season'] == selected_season]

# 🎯 STATISTIK RINGKAS
st.subheader("📊 Statistik Ringkasan")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📅 Hari dalam Dataset", value=len(filtered_df))
with col2:
    st.metric(label="🚲 Total Penyewaan Sepeda", value=filtered_df["cnt"].sum())
with col3:
    st.metric(label="🔁 Rata-rata Penyewaan", value=round(filtered_df["cnt"].mean(), 2))

st.write("Berikut adalah ringkasan statistik data penyewaan sepeda berdasarkan musim yang dipilih:")
st.dataframe(filtered_df.describe())

# 🎯 VISUALISASI 1: Penyewaan Sepeda Berdasarkan Musim
st.subheader("📌 Jumlah Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=df_day["season"], y=df_day["cnt"], estimator=sum, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Total Penyewaan Sepeda per Musim")
st.pyplot(fig)

# 🎯 VISUALISASI 2: Penyewaan Sepeda di Hari Kerja vs Akhir Pekan
st.subheader("📅 Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=df_day["workingday"], y=df_day["cnt"], estimator=sum, palette=["#ff9999", "#66b3ff"], ax=ax)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Akhir Pekan / Libur", "Hari Kerja"])
ax.set_xlabel("Kategori Hari")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Perbandingan Penyewaan Sepeda pada Hari Kerja & Akhir Pekan")
st.pyplot(fig)

# 🎯 VISUALISASI 3: Penyewaan Sepeda Berdasarkan Jam
st.subheader("⏰ Jumlah Penyewaan Sepeda Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_hour, x="hr", y="cnt", ci=None, estimator=sum, color="blue", marker="o", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Tren Penyewaan Sepeda Berdasarkan Jam")
st.pyplot(fig)

# 🎯 KESIMPULAN
st.subheader("📌 Kesimpulan")
st.write("""
- **Musim** memengaruhi jumlah penyewaan sepeda secara signifikan.  
- Penyewaan sepeda lebih **tinggi pada hari kerja** dibandingkan akhir pekan.  
- Puncak penyewaan terjadi pada **jam sibuk (pagi dan sore hari)**, sesuai dengan aktivitas komuter.
""")
