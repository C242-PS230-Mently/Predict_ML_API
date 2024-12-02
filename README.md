# Predict-ML API
Repository for machine learning API Model to Deploy in CC
# API for Determining Stress Levels : Mently App
This is a repository for hosting Machine Learning model APIs that will be deployed and can be used in applications.
## Overview
By using this API, it will bring up the results of determining a person's stress level based on the answers to the questions they have answered in the application. The results will appear in the application in the form of charts for 5 mental health disorders.

## Table of Contents

- [Setup](#setup)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Endpoints](#endpoints)
- [License](#license)

## Setup

### Requirements
To install all the libraries needed in this model, use the syntax below:
```bash
pip install -r requirements.txt
```
### Installation
```bash
# Clone the repository
git clone https://github.com/C242-PS230-Mently/Predict_ML_API.git

# Change directory
cd Predict_ML_API # change with your folder name

# Install dependencies
pip install -r requirements.txt
```
## Usage

There are a few things that need to be done to use this API:
1. Run the Flask API
   ```bash
   python app.py
    ```
   The API will be accessible at `http://127.0.0.1:5000`.
2. Make a POST request to `http://127.0.0.1:5000/predict` with input data in JSON format:
   ```plaintext
   {
    "Q1": 2, "Q2": 2, "Q3": 2, "Q4": 2, "Q5": 2,
    "Q6": 1, "Q7": 1, "Q8": 1, "Q9": 1, "Q10": 1,
    "Q11": 3, "Q12": 3, "Q13": 3, "Q14": 3, "Q15": 3,
    "Q16": 1, "Q17": 1, "Q18": 1, "Q19": 1, "Q20": 1,
    "Q21": 1, "Q22": 1, "Q23": 1, "Q24": 1, "Q25": 1
    }

   ```
   The API will display the prediction results (anxiety level, depression level, bipolar level, schizophrenia level, OCD level).
## Model
The machine learning model `(Model_Fix_RF_TF.pkl)` is loaded during API initialization and used for predictions.

## Endpoints
- **Endpoint**: /predict
- **Method**: POST
- **Input**: JSON data with features for prediction
- **Output**: ``` {
    "message": "Prediksi berhasil",
    "predictions": {
        "Level Bipolar": 3,
        "Level Depresi": 1,
        "Level Kecemasan": 3,
        "Level OCD": 2,
        "Level Skizofrenia": 2,
        "Nama Solusi": "Solusi 7: Konsultasi Psikolog untuk Terapi Intensif",
        "Solusi": "Pertimbangkan untuk konsultasi dengan psikolog untuk sesi terapi yang lebih intens. Cobalah untuk melibatkan diri dalam aktivitas sosial yang positif dan menyenangkan, serta tetap menjaga pola makan sehat dan tidur yang cukup."
    },
    "statusCode": 200

} ```


## License
Copyright © 2024 Mently Group . All rights reserved.



