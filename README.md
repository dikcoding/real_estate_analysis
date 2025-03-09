# Real Estate Price Prediction

## About the Project

The real estate market, such as in Sydney and Melbourne, presents exciting opportunities for data analysts to analyze and predict property price trends. Property price prediction is becoming increasingly important and beneficial, as property prices serve as a key indicator of the overall market condition and a country's economic health.

In this project, we process a large volume of property sales records stored in an unknown format with potential data quality issues. The main objective of this project is to clean the data, train a prediction model, and generate accurate property price forecasts.

## Stages of House Price Prediction

1. **Data Preprocessing** (`preprocess.py`)

   - Cleans and formats the data for analysis.
   - Handles missing values or anomalies in the dataset.
   - Converts unknown data formats into usable structures.

2. **Model Training** (`train.py`)

   - Trains a machine learning model to predict property prices based on the cleaned dataset.
   - Uses regression algorithms or other suitable techniques for real estate data analysis.

3. **Price Prediction** (`predict.py`)

   - Uses the trained model to predict house prices based on specific inputs.
   - Validates prediction results with actual data to measure model accuracy.

4. **Running the Program** (`main.py`)
   - Provides the main interface for executing the prediction process.
   - Integrates all stages for a complete end-to-end solution.

## Requirements

- Python 3.x
- Pandas
- Scikit-learn
- NumPy
- Matplotlib (optional, for data visualization)

## How to Use

1. Ensure all dependencies are installed:

   ```bash
   pip install -r requirements.txt

   ```

2. Run preprocessing to clean the data:

   ```bash
   python preprocess.py
   ```

3. Train the model using the cleaned dataset:

   ```bash
   python train.py
   ```

4. Use the trained model to predict house prices:
   python predict.py --input data/input.json

   ```bash
   python predict.py
   ```

5. Run the main program:
   ```bash
   python main.py
   ```

## Contribution

If you would like to contribute to this project, please fork this repository and submit a pull request with any changes or improvements.

## License

This project is released under the MIT License. Please refer to the LICENSE file for more details.

## Project Directory Structure
