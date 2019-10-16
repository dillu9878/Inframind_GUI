# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:22:13 2019

@author: Amritanjali
"""

import pickle
from sklearn.externals import joblib 
#knn_from_joblib = joblib.load('cnnfile.pkl')  
import numpy as np
from PIL import Image
import PIL
import os



class Sample:
    def __init__(self):
        self.name = ''
        self.price = 0.0
        self.discount=0.0  
        self.values = None 

class Customer:
    def __init__(self):
        self.total = 0
        self.s = ''
    
    
    def pre(self, img):
        print(img)
        img = Image.open(img)
        #img = img.convert('L')
        
        img = img.resize((64, 64), PIL.Image.ANTIALIAS)
        arr = np.array(img)
        img = np.reshape(img, (1, 64, 64, 3))
        img = img / 255

        result = classifier.predict(img)
        
        if result[0][0] < 0.5:
            prediction=colagte_V
            
        else:
            prediction = colagte_CP
            
            
        return prediction.name, prediction.price-prediction.discount
        '''
        return 'Done', 1
        '''
        
    def bill(self):
        l = len(os.listdir('./Image/'))
        count = len(os.listdir(f'./Image/customer_id{l}/'))

        self.s = 'S.N' +' '*5 + 'Product Name' + ' '*5 + 'Price\n'
        for i in range(1, count + 1):
            img = './Image/customer_id{}/input{}.jpeg'.format(l, i)
            
            name, value = self.pre(img)
            
            self.s  = self.s + f'{i}.' + ' '*5 + f'{name}      {value}\n'
            
            self.total = self.total + value
            
        
        print(self.s)
        
        print('total: ', self.total)

        dil = len(os.listdir('./Billing/')) + 1
        os.mkdir(f'./Billing/customer_id{dil}')

        f = open(f'./Billing/customer_id{dil}/billing.txt', 'w')
        f.write(self.s)
        f.write('\n' + ' '*8 + 'Total:   ' + str(self.total))
        f.close()
        
        




def main():
    
    colagte_CP = Sample()
    colagte_CP.name = "Colgate Cavity Protection"
    colagte_CP.price=10
    colagte_CP.discount=0
    
    colagte_V = Sample()
    colagte_V.name = "Colgate Vedshakti"
    colagte_V.price = 20
    colagte_V.discount=5
    
    
    
    customer_1 = Customer()
    customer_1.bill()
   
   
if __name__ =='__main__':
    main()

    
    
    
    
    