import pandas as pd
import numpy as np


class Metadata:
     
     def __init__(self, data: pd.DataFrame): 
        self._data = data 
        
    
     # @abstractmethod
     # def execute(self): 
        # pass

class RowsColumns(Metadata):
 
    def execute(self):
        return f"The number of rows of the dataset is {self._data.shape[0]} while the number of columns is {self._data.shape[1]}"            #(number of rows, number of columns)

class ColumnLabel(Metadata):   

    def execute(self):
        l = []
        for i in self._data.columns:
            l += [i] 
        return f"The labels of the columns are: {l}"
        
class Distinct(Metadata): 

    def execute(self):
       l = self._data.to_numpy()
       column = l[:,:1]
       final = np.unique(column)
       lf = []
       for i in final:
            lf += [i]
       final_distinct = (len(final),lf)
       return final_distinct
  

class Sentence(Metadata):
    
    # def __init__(self,data,id_symbol= 1):
        # Metadata.__init__(self,data)
        # self.id_symbol = id_symbol
  
    def execute_input(self,id_symbol):   #LOOK AT THIS BETTER
        l = [] 
        #id_symbol = eval(input("Give me an ID or symbol: "))
        
        for index_number in range(len(self._data)): #loops over all the indices of the df
            if self._data.iat[index_number, 0] == int(id_symbol): # .iat gives the element of column 0 , at 'index_number'
                l.append(self._data.iat[index_number, 1])
      
        
        for index_number in range(len(self._data)): #loops over all the indices of the df
            if self._data.iat[index_number, 4] == str(id_symbol): # .iat gives the element of column 0 , at 'index_number'
                l.append(self._data.iat[index_number, 1] ) #append the element that is found in column 1, at 'index_number'
    
       
        if not l: #empty lists are considered 'False', so if 'l' is empty then:
            return "No such gene ID or symbol in the dataframe"
        
        return f"{len(l)} sentences found: {l}"


class Merge(Metadata):
    
    def associations(self): 
        a = self._data[['gene_symbol', 'disease_name']].value_counts()[:10].index
        dataframe_a = pd.DataFrame(a, columns = ['Associations: (Gene,Disease)'])
        return dataframe_a

class AssociatedDisease(Metadata):
    def associate_disease(self, gene):
        if type(gene) == int:
            if (int(gene) in set(self._data['geneid'].unique())) :
                l = (self._data).loc[self._data['geneid'] == gene]
                g = l['disease_name'].tolist()
                new_l = []
                c = 0
                for i in g:
                    if g[c] not in new_l:
                        new_l.append(g[c])
                        c += 1
                    else:
                        c += 1
                return new_l
            else:
                return('The gene is not present in the dataset')
        if type(gene) == str:
            #if self._data.iat[index_number, 7] == str(gene):
            if (str(gene) in set(self._data['gene_symbol'].unique())):
                l = (self._data).loc[self._data['gene_symbol'] == gene]
                g = l['disease_name'].tolist()
                new_l = []
                c = 0
                for i in g:
                    if g[c] not in new_l:
                        new_l.append(g[c])
                        c += 1
                    else:
                        c += 1
                return new_l
            else:
                return('The gene is not present in the dataset')
        

class AssociatedGene(Metadata):
    def associate_gene(self, disease):
            if (str(disease) in set(self._data['diseaseid'].unique())) :
                l = (self._data).loc[self._data['diseaseid'] == disease]
                g = l['gene_symbol'].tolist()
                new_l = []
                c = 0
                for i in g:
                    if g[c] not in new_l:
                        new_l.append(g[c])
                        c += 1
                    else:
                        c += 1
                return new_l

            if (str(disease) in set(self._data['disease_name'].unique())):
                l = (self._data).loc[self._data['disease_name'] == disease]
                g = l['gene_symbol'].tolist()
                new_l = []
                c = 0
                for i in g:
                    if g[c] not in new_l:
                        new_l.append(g[c])
                        c += 1
                    else:
                        c += 1
                return new_l
            else:
                return('The disease is not present in the dataset')
