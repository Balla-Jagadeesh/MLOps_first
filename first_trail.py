import mlflow
def calculate_sum(x,y):
    return x+y
if __name__=='__main__':

    with mlflow.start_run():
        #starting the server of ml flow 
        x,y=10,20
        z=calculate_sum(x,y)
        #tracking the  exp
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_metric("z",z)
    