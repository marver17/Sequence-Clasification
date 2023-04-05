import numpy as np
import matplotlib.pyplot as plt
from pydicom import dcmread
import pandas as pd

class Dataset_preparation() :
    
    def __init__(self,path) :
        self.path = path
        self.__pixel_image = None
        self.__meta_image = None
    
    
    
    def load_image(self) : 
        
        ds = dcmread(self.path)
        self.__pixel_image = ds.pixel_array
        del ds.PixelData
        self.__meta_image = ds
        
        return self.__pixel_image
        
        
    def visualize_image(self):
        if self.__pixel_image is None :
            img,_ = self.load_image()
        else : 
            img = self.__pixel_image
        plt.imshow(img,cmap ="gray")
    
    def meta_info(self,param) : 
        if self.__meta_image is None :
             _ , meta = self.load_image()
        else : 
            meta = self.__meta_image
        print (meta[param])
        

    def extract_meta_info(self,param_list):
        
        tag = []
        value  = []
        if self.__meta_image is None : 
            _, meta = self.load_image()
        else  : 
            meta = self.__meta_image
        for param in param_list : 
            tag.append(f"{meta[param].tag}")
            value.append(meta[param].value)
            
        return  pd.DataFrame({"Tag":tag, "Param": param_list, "Value" : value})

