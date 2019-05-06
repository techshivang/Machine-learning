import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import warnings
print("hello world")
warnings.filterwarnings(action="ignore")
def get_data(file_name):
    dataframe=pd.read_csv(file_name)
    print(dataframe)
    x_parameter=[]
    y_parameter=[]
    for single_square_feet,single_price_value in zip(dataframe['square_feet'],dataframe['price']):
        x_parameter.append([float(single_square_feet)])
        y_parameter.append(float(single_price_value))
        return x_parameter,y_parameter
def linear_model_main(X_parameter,Y_parameter,predict_values):
    regr=linear_model.LinearRegression()
    print("AREA:",X_parameter)
    print("PRICE:",Y_parameter)
    regr.fit(X_parameter,Y_parameter)
    predict_outcome=regr.predict([[predict_values]])
    prediction={}
    prediction['coefficient']=regr.coef_
    prediction['intercept']=regr.intercept_
    prediction['predicted_values']=predict_outcome
    print("Output from Machine=",predict_outcome)
    plt.scatter(X_parameter,Y_parameter,color="m",marker="o",s=30)
    all_predicted_Y=regr.predict(X_parameter)
    plt.scatter(X_parameter,all_predicted_Y,color="b")
    plt.plot(X_parameter,all_predicted_Y,color="r")
    plt.scatter(predict_values,predict_outcome,color="g")
    plt.show()
    return prediction
if __name__=="__main__":
    x,y=get_data('LR_House_price.csv')
    predict_value=700
    result=linear_model_main(x,y,predict_value)
    print("Intercept value",result['intercept'])
    print("coefficient",result['coefficient'])
    print("Predicted House Price value:",result['predicted_values'])