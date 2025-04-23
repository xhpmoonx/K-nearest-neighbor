# K-Nearest Neighbor (KNN) Implementation

This repository contains a Python implementation of the K-Nearest Neighbor (KNN) algorithm from scratch. It demonstrates how the KNN algorithm works without relying on external machine learning libraries.

## 📁 Project Structure

```
K-nearest-neighbor/
├── knn.py              # Core implementation of the KNN algorithm
├── data.csv            # Sample dataset used for testing
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/xhpmoonx/K-nearest-neighbor.git
   cd K-nearest-neighbor
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the KNN script:

   ```bash
   python knn.py
   ```

## 🧠 Algorithm Overview

The K-Nearest Neighbor algorithm is a simple, non-parametric, and lazy learning algorithm used for classification and regression. It operates by finding the 'k' closest data points in the training set to a new input and making predictions based on majority voting (for classification) or averaging (for regression).

### Key Features:

- **Distance Metrics**: Calculates distances between data points using metrics like Euclidean, Manhattan, or Minkowski distances.
- **Parameter 'k'**: The number of nearest neighbors to consider for making predictions.
- **No Training Phase**: KNN does not require a training phase; it stores the entire dataset and makes predictions at runtime.

## 📊 Example Usage

Assuming `data.csv` contains your dataset:

```bash
python knn.py
```

The script will:

1. Load the dataset.
2. Split the data into training and testing sets.
3. Predict the class of test instances using the KNN algorithm.
4. Output the accuracy of the model.

