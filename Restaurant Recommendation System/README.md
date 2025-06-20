# **Restaurant Recommendation System**
---
## **Project Description**

-This project presents an intelligent Restaurant Recommendation System designed to help users make smarter dining choices. The system suggests restaurants based on:

-User preferences (like food type, ambiance)

-Budget

-Dietary restrictions

-Current location

-A hybrid recommendation model has been implemented, combining the power of:

-Collaborative Filtering (user-based insights)

-Content-Based Filtering (restaurant metadata)

The system dynamically adapts to input and geo-location data to generate accurate and relevant restaurant recommendations.

## **Screenshots**
 Home Page
<p align="center">

 <img src="https://drive.google.com/uc?export=view&id=198vsiW24dMOjFzE5roUvwiLdrcfe_nKt" width="800" alt="Home Page"> 
 </p>
 Input Page
<p align="center">
 <img src="https://drive.google.com/uc?export=view&id=1ASQvbRIgYDzxWXl7yeHjMjUC2H4kGw7D" width="800" alt="Input Page"> 
 </p>
 Recommendation Output
<p align="center"> 
<img src="https://drive.google.com/uc?export=view&id=1MzZvnK9bnpfMscLcJTGuGzLBZxsiERjG" width="800" alt="Recommendation Output">
 </p>

## **Installation and Setup**

### Using Conda (Recommended)
```bash
# Create a new conda environment
conda create -n restaurant_recommender python=3.10


# Activate the environment
conda activate restaurant_recommender

# Clone the repository
git clone https://github.com/Simrannayak647/Restaurant-Recommendation-System.git
cd Restaurant-Recommendation-System/Flask

# Install dependencies
pip install -r requirements.txt
```
### Using Python venv
```bash
# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Navigate to the Flask directory
cd Flask

# Run the Flask web application
python app.py

# Visit http://localhost:5000 to access the app
```
### Project Structure:

```bash
Restaurant-Recommendation-System/
├── 6.Final Report & Demo Link
├── Flask/
│   ├── __pycache__/                # Compiled Python cache files
│   ├── static/                     # Static assets (Images)
│   ├── templates/                  # HTML templates for the frontend
│   ├── app.py                     # Flask application entry point
│   ├── Final_Development_Phase.ipynb  # Flask dev notebook
│   ├── requirements.txt            # Python dependencies
│   └── restaurant1.csv             # Restaurant dataset
├── Model/
    └── Final_Development_Phase.ipynb  # Model training and evaluation notebook
```

## **🧰 Technologies Used**
- **Category**	Tools & Libraries
- **Language**	Python 3.10
-**Web Framework**	Flask
-**ML/Recommendation**	Scikit-learn, Surprise (SVD)
-**Data Handling**	Pandas, NumPy
-**NLP	NLTK**
-**Visualization**	Matplotlib, Seaborn, Plotly
-**Frontend**	HTML, CSS, JavaScript

---

## **Model Architecture**
This project uses a **Hybrid Recommendation Model** combining the strengths of:

###🔹 Content-Based Filtering

Matches restaurants to user preferences (cuisine, rating, price).

###🔹 Collaborative Filtering (SVD)

Suggests restaurants based on similar user behaviors.

###🔹 Hybrid Model (Selected)

Combines both approaches for accuracy and personalization.

Solves cold-start and sparsity issues.
---
## **Dataset**
The dataset is sourced from **Kaggle** and titled:

> [Zomato Bangalore Restaurants Dataset by Himanshu Poddar](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants)


### **📌 Conclusion**

This system simplifies the task of choosing a restaurant by offering intelligent, data-driven suggestions based on user needs. It bridges the gap between decision fatigue and enjoyable dining. The hybrid recommendation model ensures accuracy, diversity, and scalability.




