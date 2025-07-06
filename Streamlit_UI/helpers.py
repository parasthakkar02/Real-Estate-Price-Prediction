import os
import pickle
import json
import numpy as np

locations = None
data_columns = None
model = None


def load_files():
    global locations, data_columns, model

    with open(
        os.path.join(os.path.dirname(__file__), "../Model/columns.json"), "r"
    ) as f:
        data_columns = json.load(f)["data_columns"]
        locations = data_columns[3:]

    if model == None:
        with open(
            os.path.join(
                os.path.dirname(__file__),
                "../Model/banglore_home_prices_model.pickle",
            ),
            "rb",
        ) as f:
            model = pickle.load(f)


def get_locations():
    load_files()
    return locations


def predict_price_function(location, area, bhk, bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1  # for other locations

    x = np.zeros(len(data_columns))
    x[0] = area
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)


if __name__ == "__main__":
    load_files()
    print(predict_price_function("1st Phase JP Nagar", 1000, 3, 3))
#     print(predict_price_function("Kalhalli", 1000, 2, 2))  # other location
