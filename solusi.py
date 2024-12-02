from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Memuat model Random Forest
rf_models = joblib.load('Model_Fix_RF_TF.pkl')

# Definisi fungsi untuk menghitung solusi berdasarkan jumlah total level
def calculate_solusi(lv1, lv2, lv3, lv4, lv5):
    total_level = lv1 + lv2 + lv3 + lv4 + lv5
    if total_level == 5:
        return {
            'Nama Solusi': 'Solusi 1: Aktivitas Fisik Ringan dan Tidur Cukup',
            'Solusi': "Lakukan aktivitas fisik ringan seperti jalan kaki dan pastikan tidur yang cukup. Cobalah untuk menjaga rutinitas sehari-hari dan hindari stres berlebihan."
        }
    elif total_level == 6:
        return {
            'Nama Solusi': 'Solusi 2: Latihan Pernapasan dan Meditasi',
            'Solusi': "Latihan pernapasan dalam dan meditasi dapat membantu meredakan kecemasan. Cobalah meluangkan waktu untuk diri sendiri, seperti berendam air hangat atau mendengarkan musik yang menenangkan."
        }
    elif total_level == 7:
        return {
            'Nama Solusi': 'Solusi 3: Yoga dan Olahraga Ringan',
            'Solusi': "Cobalah melakukan yoga atau olahraga ringan untuk mengurangi ketegangan. Luangkan waktu untuk berjalan di luar ruangan dan menikmati alam. Berbicara dengan teman dekat juga bisa membantu."
        }
    elif total_level == 8:
        return {
            'Nama Solusi': 'Solusi 4: Konsultasi dengan Terapis',
            'Solusi': "Pertimbangkan untuk berkonsultasi dengan seorang konselor atau terapis. Terapkan teknik relaksasi, seperti pernapasan diafragma, untuk membantu menenangkan pikiran. Jangan ragu untuk mencari dukungan dari orang terdekat."
        }
    elif total_level == 9:
        return {
            'Nama Solusi': 'Solusi 5: Terapi Perilaku Kognitif (CBT)',
            'Solusi': "Ikuti sesi terapi perilaku kognitif (CBT) untuk membantu mengatasi pola pikir negatif. Cobalah untuk lebih terbuka dengan orang terdekat tentang perasaan Anda. Juga, pastikan untuk makan makanan bergizi untuk mendukung kesejahteraan mental."
        }
    elif total_level == 10:
        return {
            'Nama Solusi': 'Solusi 6: Kegiatan Sosial dan Dukungan Keluarga',
            'Solusi': "Luangkan waktu untuk berkumpul dengan keluarga atau teman untuk meningkatkan dukungan sosial. Melakukan kegiatan yang menyenangkan bersama orang-orang terdekat bisa memberikan rasa nyaman dan mengurangi stres."
        }
    elif total_level == 11:
        return {
            'Nama Solusi': 'Solusi 7: Konsultasi Psikolog untuk Terapi Intensif',
            'Solusi': "Pertimbangkan untuk konsultasi dengan psikolog untuk sesi terapi yang lebih intens. Cobalah untuk melibatkan diri dalam aktivitas sosial yang positif dan menyenangkan, serta tetap menjaga pola makan sehat dan tidur yang cukup."
        }
    elif total_level == 12:
        return {
            'Nama Solusi': 'Solusi 8: Terapi Intensif dengan Psikiater',
            'Solusi': "Mulailah terapi intensif dengan seorang psikiater yang berpengalaman. Cobalah mengatur waktu untuk beristirahat dan menjaga kesehatan fisik. Mengikuti kelompok dukungan juga dapat membantu untuk berbagi pengalaman dan mendapatkan perspektif baru."
        }
    elif total_level == 13:
        return {
            'Nama Solusi': 'Solusi 9: Pengobatan Medis untuk Gangguan Mental',
            'Solusi': "Disarankan untuk mulai menjalani pengobatan medis untuk gangguan mental. Penting untuk mengikuti jadwal terapi dan pengobatan yang diberikan oleh dokter. Cobalah untuk tetap aktif dalam kegiatan positif dan mencari dukungan dari keluarga atau teman."
        }
    elif total_level == 14:
        return {
            'Nama Solusi': 'Solusi 10: Perawatan Intensif dan Terapi Rawat Inap',
            'Solusi': "Dapatkan perhatian medis lebih lanjut melalui terapi intensif atau rawat inap. Fokuskan diri pada perawatan penuh dan diskusikan rencana perawatan dengan tenaga medis yang berkompeten. Melibatkan keluarga dalam proses penyembuhan juga sangat membantu."
        }
    elif total_level == 15:
        return {
            'Nama Solusi': 'Solusi 11: Perawatan Medis Penuh dan Rawat Inap',
            'Solusi': "Pertimbangkan perawatan medis penuh atau rawat inap untuk penanganan jangka panjang. Jangan ragu untuk mencari bantuan medis secara intensif dan mengikuti semua instruksi profesional. Fokuskan diri pada pemulihan dan bangun sistem dukungan yang kuat di sekitar Anda."
        }

# Definisi route untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil data input dari request (JSON)
        data = request.get_json(force=True)
        
        # Membuat DataFrame dari input yang diterima
        input_data = pd.DataFrame([data])

        # Memastikan input_data memiliki format yang benar
        if input_data.shape[1] != 25:
            return jsonify({'error': 'Input data harus memiliki 25 fitur'}), 400

        # Melakukan prediksi untuk setiap gangguan menggunakan model Random Forest
        prediksi = {}
        level_gangguan = {}
        
        for gangguan in rf_models.keys():
            model = rf_models[gangguan]
            prediksi[gangguan] = int(model.predict(input_data)[0])  # Prediksi level gangguan
            level_gangguan[gangguan] = prediksi[gangguan]

        # Menghitung solusi berdasarkan total level
        total_level = sum(level_gangguan.values())
        solusi = calculate_solusi(level_gangguan['Level Kecemasan'], 
                                  level_gangguan['Level Depresi'], 
                                  level_gangguan['Level Bipolar'], 
                                  level_gangguan['Level Skizofrenia'], 
                                  level_gangguan['Level OCD'])

        # Mengembalikan hasil prediksi dan solusi
        return jsonify({
            'statusCode': 200,
            'message': 'Prediksi berhasil',
            'predictions': {
                'Level Kecemasan': prediksi['Level Kecemasan'],
                'Level Depresi': prediksi['Level Depresi'],
                'Level Bipolar': prediksi['Level Bipolar'],
                'Level Skizofrenia': prediksi['Level Skizofrenia'],
                'Level OCD': prediksi['Level OCD'],
                'Nama Solusi': solusi['Nama Solusi'],
                'Solusi': solusi['Solusi']
            }
        }), 200

    except Exception as e:
        # Menangani error yang mungkin terjadi
        return jsonify({
            'statusCode': 500,
            'message': 'Terjadi kesalahan',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Menjalankan aplikasi Flask di port 5000
    app.run(debug=True, port=5000)
