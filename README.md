
Deploying a Machine Learning Model Using FastAPI

main.py

In this FastAPI code, I've created a machine learning model that can predict the species of an iris flower based on its features (sepal length, sepal width, petal length, and petal width). I've saved this trained model as a .pkl file using joblib. The FastAPI application loads this model and uses it to make predictions when it receives input data in the specified format.
•	The FastAPI application defines a data model (IrisInput) to structure the input data.
•	It loads the pre-trained model from the trainedModel.pkl file.
•	It sets up an API endpoint (/predict) that takes input data, uses the model to predict the iris flower's species, and returns the result.
•	If there's any issue with the prediction process, it returns an appropriate error message.


GIT Hub link :- https://github.com/SerujanSatkunanathan/fast-api-Railway-model-deployement


Deployed App Link :- https://trustworthy-dream-production.up.railway.app/


 


![image](https://github.com/user-attachments/assets/0cd5ea5e-11ed-428d-854a-e70439086f73)

![image](https://github.com/user-attachments/assets/d1cb3ed9-7e8c-4e0b-8b5e-c5c673da1cfc)
![image](https://github.com/user-attachments/assets/bd7d5d83-b5b6-4441-93d0-e6a515d01c1e)

![image](https://github.com/user-attachments/assets/4d94254f-776c-48b5-a7f1-a44b00be8510)
![image](https://github.com/user-attachments/assets/6aa51845-4572-451d-8c26-fbe15943ba6b)


