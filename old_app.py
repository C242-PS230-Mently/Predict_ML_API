from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Memuat seluruh model dari file
models_loaded = joblib.load('Model_Fix_RF_TF.pkl')

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

        # Melakukan prediksi untuk setiap gangguan
        prediksi = {}
        for gangguan in models_loaded.keys():
            model = models_loaded[gangguan]
            prediksi[gangguan] = int(model.predict(input_data)[0])

        # Mengembalikan hasil prediksi
        return jsonify({
            'statusCode': 200,
            'message': 'Prediksi berhasil',
            'predictions': prediksi
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


'''
{
    "Q1": 2, "Q2": 2, "Q3": 2, "Q4": 2, "Q5": 2,
    "Q6": 1, "Q7": 1, "Q8": 1, "Q9": 1, "Q10": 1,
    "Q11": 3, "Q12": 3, "Q13": 3, "Q14": 3, "Q15": 3,
    "Q16": 1, "Q17": 1, "Q18": 1, "Q19": 1, "Q20": 1,
    "Q21": 1, "Q22": 1, "Q23": 1, "Q24": 1, "Q25": 1
}

output
{
    "message": "Prediksi berhasil",
    "predictions": {
        "Level Bipolar": 3,
        "Level Depresi": 1,
        "Level Kecemasan": 2,
        "Level OCD": 1,
        "Level Skizofrenia": 1
    },
    "statusCode": 200
}
'''