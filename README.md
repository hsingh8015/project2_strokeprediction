# Project 2: Stroke Prediction
#### September 27, 2024

### Authors
Danielle Dejean\
Kaidon Kennedy\
Carolyn Scheese\
Harpreet 'Monty' Singh

### Acknoweldgements 
Special thanks to Bill Parker (Instructor) & Sean Myers (TA) for help trouble shooting this project and it's various parts. 
Note: X-Pert, ChatGPT & Google Colab AI were used in creating this project. 

### Technical Skills
- Jupyter Notebook
- Python
- Splitting data into training and testing sets
- Scaling features 
- Selecting a model 
- Streamlit app development 

### Project Description 
Ischemic strokes have a tremendous impact on individuals, families and society. Individuals who experience a stroke often face loss of independence, physical disabilities, cognative impairment, communication challenges, depression and anxiety, and social withdrawel due to embarrassment or frustation over new limitations. Families are impacted when a loved one experiences a stroke. They often assume additional responsibilities assuming the role of caregiver, experiencing social isolation, and experience a financial strain due to an increase in healthcare costs and possible loss or decrease in employment, as well as a resulting emotional toll. Strokes represent one of Society's Public Health Challenges. Strokes place a burden on our healthcare system. Healthcare direct costs for stokes in the United States are estimated at $34 billion annually. Indirect costs (eg, loss of productivity due to disabilty or premature death) can amount to an additional $16 billion. 

>The impact of strokes is profound and multifaceted, affecting not just the individual but also their family and society at large. These challenges underscore the importance of preventive measures, early detection through predictive modeling (like our AI project), and comprehensive support systems for stroke survivors and their families. By addressing these areas, we can work towards reducing the burden of stroke and improving outcomes for everyone affected.

_The purpose of this project is to create a model that will be the under pinning's for predicting an individualized risk of ischemic stroke.
This model will then be the basis of a Streamlit app (prototype) that can then be used to predict individual risk for stroke based off major risk factors so that steps can be taken early, to make changes in modifiable risks._
                  
### Installation & Usage
The files within the Project2_strokeprediction repo were updated using Python version 3.10.14, in Google Collab and Jupyter Notebook. To run it please download the most recent version of Python, as well as a code editor that runs Python (Visual Studio Code, PyCharm, etc.). To run Google Collab, create and link your Google account, then open Google Drive - select "new >> more >> Google Colaboratory".

Create Repo in GitHub. Include .gitignore/ secrets.toml, for housing API keys in Streamlit

Open Jupyter Notebooks 
Install the following libraries & tools 
<img src="images\Items_to_import.jpg">

Download .csv file from Kaggle, read into a df
<img src="images\reading_data.jpg">

Copy Data and drop NAN and id rows
<img src="images\copy_data_dropNa_id.jpg">    

### Run Instructions:
    Terminal (Mac) or GitBash (Windows):
    Ensure that you're running the correct version of Python (see above)
    Ensure that you're in the directory containing the file before running

### Steps 
OneHotEncoder
<img src="images\OneHotEncoder.jpg">

Split the data into training and test sets
<img src="images\splitting_data_train_test.jpg">

Use Smote to balance data
<img src="images\applying_SMOTE.jpg">

Gradient Boost Classifier
<img src="images\GradienrBoostingClassifier.jpg">

Use Gradient Boost for best overall accuracy and prediction
<img src="images\GradientBoostAccuracy_confusionMatrix.png">
        

## Streamlit App
NOTE: be sure your features are in the same order. 
[Streamlit App](https://project2strokeprediction.streamlit.app/)
<img src="images\stroke_risk_prediction_app.jpg">

### Challenges 
1. One of the big challenges encountered was our data was so imbalanced that every model that was trained was so accurate that it did not properly predict the minority class correctly because of what it had been trained on. Hypertuning of parameters were predicted at 12%.
Resolution: We used SMOTE to help balance data
2. We had issues with pushing to github because of branch and .DS_Store file (Mac only) synchronization. 
Resolution: The .DS file can get deleted or added to .gitignore
3. Printing decision tree graphic 
Resolution: We were able to print it using Google Colab
4. We had problems representing binary data as user input in Streamlit app 
Resolution: Mapping for categorical features to numeric values 
5. Getting the Streamlit app to properly predict Stroke Risk
Resolution: needed proper sequencing of features.

### References 
1. [Data Source](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
2. [UpToDate. Overview of Secondary Prevention of Ischemic Stroke](https://www-uptodate-com.ezproxy.lib.utah.edu/contents/overview-of-secondary-prevention-of-ischemic-stroke?search=stroke%20risk%20factors&source=search_result&selectedTitle=1%7E150&usage_type=default&display_rank=1)
3. [WHO. (2024). Mean Fasting Blood Glucose](https://www.who.int/data/gho/indicator-metadata-registry/imr-details/2380#:~:text=The%20expected%20values%20for%20normal,and%20monitoring%20glycemia%20are%20recommended)
4. [Northcott S, Moss B, Harrison K, Hilari K. A systematic review of the impact of stroke on social support and social networks: associated factors and patterns of change. Clinical Rehabilitation. 2016;30(8):811-831. doi:10.1177/0269215515602136](https://pubmed.ncbi.nlm.nih.gov/26330297/)