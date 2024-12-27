# Crystal Clear Vision: Revolutionizing Cataract Prediction through Transfer Learning Mastery

## Overview
Crystal Clear Vision is a web application designed to assist in the early detection of cataracts using the power of deep learning. By leveraging pre-trained transfer learning models, the application analyzes eye images and provides a prediction of cataract presence.

## Features
- Upload eye images for cataract prediction.
- Utilizes a pre-trained VGG19 model for image classification.
- Provides a user-friendly interface for easy navigation and interaction.

## Installation

### Prerequisites
- Python 3.6 or higher
- Flask
- TensorFlow
- Pillow
- NumPy

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/balamanikantsai/Crystal-Clear-Vision-Revolutionizing-Cataract-Prediction-through-Transfer-Learning-Mastery.git
    cd Crystal-Clear-Vision-Revolutionizing-Cataract-Prediction-through-Transfer-Learning-Mastery
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download the pre-trained VGG19 model from the [Google Drive link](https://drive.google.com/file/d/1dtsFr9nJoKo03ZIdvimI_8E-IWDKS-2j/view?usp=sharing) and place it in the project directory.

## Usage
1. Run the Flask application:
    ```sh
    python src/app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Use the navigation bar to explore the application:
    - **Home**: Introduction to the application.
    - **About**: Information about the project and the team.
    - **Prediction**: Upload an eye image to get a cataract prediction.

## Project Structure
```
Crystal-Clear-Vision/
│
├── src/
│   ├── templates/
│   │   ├── about.html
│   │   ├── details.html
│   │   ├── index.html
│   │   ├── resu.html
│   ├── app.py
│
├── README.md
├── requirements.txt
```

## Team
- Eshtamsetti Yasaswini
- Guduru Bala Manikanta Sai
- Yemireddi Abhiram
- Nithin Satya

## License
This project is licensed under the MIT License.

