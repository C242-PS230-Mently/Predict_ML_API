# Menggunakan image base Python
FROM python:3.9-slim

# Tentukan direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt dan install dependensi
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn untuk menjalankan aplikasi Flask
RUN pip install gunicorn

# Salin seluruh aplikasi ke dalam container
COPY . .

# Ekspose port yang digunakan oleh aplikasi
EXPOSE 8080

# Tentukan command untuk menjalankan aplikasi menggunakan Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
