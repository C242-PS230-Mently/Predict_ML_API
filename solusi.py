from flask import Flask, request, jsonify

app = Flask(__name__)

# Solusi berdasarkan jumlah level
def solusi_berdasarkan_jumlah_level(total_level):
    if total_level == 5:
        return "Lakukan aktivitas fisik ringan seperti jalan kaki dan pastikan tidur yang cukup."
    elif total_level == 6:
        return "Latihan pernapasan dalam dan meditasi dapat membantu meredakan kecemasan."
    elif total_level == 7:
        return "Cobalah melakukan yoga atau olahraga ringan untuk mengurangi ketegangan."
    elif total_level == 8:
        return "Pertimbangkan untuk berkonsultasi dengan seorang konselor atau terapis."
    elif total_level == 9:
        return "Ikuti sesi terapi perilaku kognitif untuk membantu mengatasi pola pikir negatif."
    elif total_level == 10:
        return "Luangkan waktu untuk berkumpul dengan keluarga atau teman untuk meningkatkan dukungan sosial."
    elif total_level == 11:
        return "Pertimbangkan untuk konsultasi dengan psikolog untuk sesi terapi yang lebih intens."
    elif total_level == 12:
        return "Mulailah terapi intensif dengan seorang psikiater yang berpengalaman."
    elif total_level == 13:
        return "Disarankan untuk mulai menjalani pengobatan medis untuk gangguan mental."
    elif total_level == 14:
        return "Dapatkan perhatian medis lebih lanjut melalui terapi intensif atau rawat inap."
    elif total_level == 15:
        return "Pertimbangkan perawatan medis penuh atau rawat inap untuk penanganan jangka panjang."

# Definisi route untuk solusi
@app.route('/solusi', methods=['POST'])
def solusi():
    try:
        # Ambil data input dari request (JSON)
        data = request.get_json(force=True)
        
        # Memastikan data yang diterima adalah prediksi gangguan
        gangguan_level = data.get('predictions', {})
        if not gangguan_level or len(gangguan_level) != 5:
            return jsonify({'error': 'Data prediksi tidak lengkap'}), 400

        # Menghitung jumlah total level
        total_level = sum(gangguan_level.values())

        # Menentukan solusi berdasarkan total jumlah level
        solusi_result = solusi_berdasarkan_jumlah_level(total_level)

        # Mengembalikan hasil solusi
        return jsonify({
            'statusCode': 200,
            'message': 'Solusi berhasil ditemukan',
            'solusi': solusi_result
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
