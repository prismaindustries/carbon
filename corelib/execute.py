__author__ = 'Prisma Overlord'
import sys
sys.path.insert(0, '/scikit-learn-master/')
import datetime
import random
import neural_net as neuralNetwork

    #Builds the gui for graph plotting data.

    #This class will control machine learning function calls and will return function values.
    #class ML_Controller(FNC_COMMAND, X_parameters, Y parameters, predict value):
    # Function for Fitting our data to Linear model
        #def linear_model_main(X_parameters,Y_parameters,predict_value):
         # Create linear regression object
            #regr = linear_model.LinearRegression()  regr.fit(X_parameters, Y_parameters)
            #predict_outcome = regr.predict(predict_value)
            #return predict_outcome;


neuralNetwork.TwoLayerNet(2,4,8)
class Application():
    # Generates log file entry, and appends to the log file if it exists.
    def __init__(self):
        log_file = 'log.txt'
        try:
            log_data = open(log_file, "wb")
            log_data.write("Log Entry: "+datetime+" > ")
            print(sys.path)
        except:
            "Appending to log file."
            with open(log_file, "a") as log_data:
                log_data.write("appended text")
    @classmethod
    def sysInfoPrinter(cls):
        print(sys.path)
    @classmethod
    def byteExtractor(cls, fileName):
        f = open(fileName, "rb")
        try:
            byte = f.read(1)
            while byte != "":
                #Do stuff with bytes
                byte = f.read(1)
                print(byte)

        finally:
            f.close()
    @classmethod
    def generator(cls,scale):
        randNum = random.randint(1,20)
        randNum = randNum*scale
        return randNum




config_file = 'config.txt'
controller = Application()
numList = controller.generator(10000)
controller.sysInfoPrinter()
print(numList)
