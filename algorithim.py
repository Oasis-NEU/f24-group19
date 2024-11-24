import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Creates an empty DataFrame for pants
def empty_pants():
    parameters = ["clothing", "top_bot", "color", "length", "style"]
    df = pd.DataFrame(columns=parameters)
    return df

# Gets all file directories in a specified directory
def directory_file(directory):
    files = os.listdir(directory)
    img_files = [os.path.join(directory, filename) for filename in files]
    return img_files

# Tags clothing images with specified parameters
def tagging(clothing, top_bot, color, length, style):
    return {
        'clothing': clothing,
        'top_bot': top_bot,
        'color': color,
        'length': length,
        'style': style
    }

# Adds tagged data to the DataFrame
def add_data(formatted, df):
    df = df._append(formatted, ignore_index=True)
    return df

# Manually tags pants images
def pants_tagging():
    pants_directory = 'clothing v.2/pants'
    pants = directory_file(pants_directory)

    # Manual tagging for each file
    formats = [
        tagging("pants 1", "bottom", "black", "shorts", "sweats"),
        tagging("pants 2", "bottom", "green", "long", "cargo"),
        tagging("pants 3", "bottom", "black", "long", "sweats"),
        tagging("pants 4", "bottom", "white", "long", "sweats"),
        tagging("pants 5", "bottom", "navy", "long", "jeans"),
        tagging("pants 6", "bottom", "light blue", "long", "jeans"),
        tagging("pants 7", "bottom", "black", "long", "jeans"),
        tagging("pants 8", "bottom", "blue", "long", "slacks"),
        tagging("pants 9", "bottom", "beige", "long", "slacks"),
        tagging("pants 10", "bottom", "gray", "long", "slacks")
    ]
    return formats

# Encodes categorical columns
def encoding(df):
    label_encoders = {}
    for column in ["clothing", "top_bot", "color", "length", "style"]:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    return df, label_encoders

# Splits and scales the dataset
def train_test(df):
    X = df.drop('clothing', axis=1)
    y = df['clothing']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, scaler

# Trains the k-NN classifier
def clothing_algo(df, n_neighbors=3):
    X_train, X_test, y_train, y_test, _ = train_test(df)
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    return knn

# Predicts the category of a new clothing item
def predict_new_item(knn, new_item, label_encoders, scaler, clothing_encoder):
    for column in ["top_bot", "color", "length", "style"]:
        new_item[column] = label_encoders[column].transform(new_item[column])
    new_item_scaled = scaler.transform(new_item.drop('clothing', axis=1))
    predicted_clothing = knn.predict(new_item_scaled)
    return clothing_encoder.inverse_transform(predicted_clothing)

# Main function
def main():
    # Initialize an empty DataFrame
    df = empty_pants()

    # Add tagged data
    formats = pants_tagging()
    for format_ in formats:
        df = add_data(format_, df)

    # Encode data
    df, label_encoders = encoding(df)

    # Train the k-NN model
    knn = clothing_algo(df)

    # Create a new item to predict
    new_item = pd.DataFrame({
        "clothing": ["new pants"],
        "top_bot": ["bottom"],
        "color": ["green"],
        "length": ["long"],
        "style": ["slacks"]
    })

    # Predict the new item's category
    _, _, _, _, scaler = train_test(df)
    predicted_item = predict_new_item(knn, new_item, label_encoders, scaler, label_encoders["clothing"])

    print(f"Predicted clothing category: {predicted_item[0]}")

if __name__ == "__main__":
    main()
