from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

# Global variables for model and encoders
knn = None
label_encoders = {}
scaler = None

# Creates an empty DataFrame for pants
def empty_pants():
    parameters = ["clothing", "top_bot", "color", "length", "style"]
    return pd.DataFrame(columns=parameters)

# Tags pants data
def pants_tagging():
    formats = [
        {"clothing": "pants 1", "top_bot": "bottom", "color": "black", "length": "shorts", "style": "sweats"},
        {"clothing": "pants 2", "top_bot": "bottom", "color": "green", "length": "long", "style": "cargo"},
        {"clothing": "pants 3", "top_bot": "bottom", "color": "black", "length": "long", "style": "sweats"},
        {"clothing": "pants 4", "top_bot": "bottom", "color": "white", "length": "long", "style": "sweats"},
        {"clothing": "pants 5", "top_bot": "bottom", "color": "navy", "length": "long", "style": "jeans"},
        {"clothing": "pants 6", "top_bot": "bottom", "color": "light blue", "length": "long", "style": "jeans"},
        {"clothing": "pants 7", "top_bot": "bottom", "color": "black", "length": "long", "style": "jeans"},
        {"clothing": "pants 8", "top_bot": "bottom", "color": "blue", "length": "long", "style": "slacks"},
        {"clothing": "pants 9", "top_bot": "bottom", "color": "beige", "length": "long", "style": "slacks"},
        {"clothing": "pants 10", "top_bot": "bottom", "color": "gray", "length": "long", "style": "slacks"}
    ]
    return pd.DataFrame(formats)

# Encodes categorical data
def encoding(df):
    global label_encoders
    label_encoders = {}
    for column in ["clothing", "top_bot", "color", "length", "style"]:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    return df

# Splits and scales data
def train_test(df):
    X = df.drop('clothing', axis=1)
    y = df['clothing']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    global scaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test

# Trains the k-NN model
def train_model(df):
    X_train, _, y_train, _ = train_test(df)
    global knn
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

# Predicts new item
def predict_new_item(new_item):
    for column in ["top_bot", "color", "length", "style"]:
        new_item[column] = label_encoders[column].transform(new_item[column])
    new_item_scaled = scaler.transform(new_item)
    predicted_clothing = knn.predict(new_item_scaled)
    return label_encoders["clothing"].inverse_transform(predicted_clothing)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    # Create and encode dataset
    df = pants_tagging()
    df = encoding(df)
    train_model(df)
    return jsonify({"message": "Model trained successfully!"})

@app.route('/predict', methods=['POST'])
def predict():
    if knn is None:
        return jsonify({"error": "Model not trained yet. Call /train first."}), 400

    # Get user input from the form
    data = request.json
    new_item = pd.DataFrame([data])

    # Predict category
    predicted_item = predict_new_item(new_item)
    return jsonify({"predicted_category": predicted_item[0]})

if __name__ == '__main__':
    app.run(debug=True)
