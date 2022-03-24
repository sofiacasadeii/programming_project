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
            if self._data.iat[index_number, 0] == id_symbol: # .iat gives the element of column 0 , at 'index_number'
                l.append(self._data.iat[index_number, 1])
      
        
        for index_number in range(len(self._data)): #loops over all the indices of the df
            if self._data.iat[index_number, 4] == id_symbol: # .iat gives the element of column 0 , at 'index_number'
                l.append(self._data.iat[index_number, 1] ) #append the element that is found in column 1, at 'index_number'
    
       
        if not l: #empty lists are considered 'False', so if 'l' is empty then:
            return "No such gene ID or symbol in the dataframe"
        
        return f"{len(l)} sentences found: {l}"

class Merge(Metadata):
    
    def associations(self): 
        a = self._data[['gene_symbol', 'disease_name']].value_counts()[:10].index
        #dataframe_a = pd.DataFrame(a, columns = ['Gene', 'Disease'])
        return a#dataframe_a
       

    
    # def distinct_disease(self):
        # list_disease = self.datadisease['diseaseid'].tolist() 
        # distinct_disease_list = []
        # for i in list_disease:
            # if i not in distinct_disease_list:
                # distinct_disease_list.append(i)
        # return sorted(distinct_disease_list)
    
    # def disease_dictionary(self):
        
        # df = self.datadisease
        
        # d = df.to_numpy()
        # smaller = d[:, [0, 3]]
        
        # dictionary2 = {}
        # for i in self.distinct_disease():
            # v = []
            # for diseaseid, pmid in zip(smaller.T[0], smaller.T[1]): 
                # if diseaseid == i:
                    # v.append(pmid)     
                # dictionary2[i] = v
            
        # return dictionary2
 
    

# class CompareDictionaries(RegistryCompare,Disease,Gene):
    
    # def __init__(self, datadisease , data):
        
        # Disease.__init__(self, datadisease)
        # Gene.__init__(self, data)
        
    # # def function(self):
        # # return self.datadisease
    
    # def compare_dictionary(self):
        
        # d3 = {}
        # d1 = self.disease_dictionary()
        # d2 = self.gene_dictionary()
        # keys_d1 = d1.values()
        # keys_d2 = d2.values()
        
        # for keys_d1 in d1: #loops over keys in d1
          # for keys_d2 in d2: #loops over keys in d2
            # if keys_d1 == keys_d2: 
                # d3[] = keys_d1



        # c = [] 
        
        # counter = 0
        # for k in sorted(d3, key=lambda k: len(d3[k]), reverse=True): #sorts the values of d3 by length
            # if counter == 10: #makes sure it returns the first 3
              # break
            # print(f"{counter + 1}. diseaseid {k[0]} and gene {k[1]} are related") 
            # counter = counter + 1
    
    # def disease_associated_gene(self):
        
        
        # # g = []
        # for key in d2:
          # g.append(list(set(d1[key]) & set(d2[key])))
          
        # return g 



# disease = ImportDisease("disease_evidences.tsv", {RowsColumns,ColumnLabel})
# print (disease.operations())
#pd_disease = (ImportDisease.pd_disease(disease))

# gene = ImportGene("gene_evidences.tsv", {Gene, CompareDictionaries})
# pd_gene = (ImportGene.pd_gene(gene))



# compare = CompareDictionaries(pd_disease,pd_gene)
# print(compare.compare_dictionary())
   



# class Disease(RegistryBuldier,Import): 
  
        
    # def sentences_disease(self, disease_id):
        # list2 = self.dataframe.data_import()['diseaseid'].tolist()
        # s = []
        # for i in list2:
            # if disease_id == i:
                # f = self.dataframe.data_import().loc[i, 'sentence']
                # s.append(f)
        # return s




# dataframe_disease = Metadata(disease)
# dataframe_gene = Gene(gene)




#import numpy as np
# class Association(Metadata):
	# def disease_list(self):
		# keys = self.dataframe.data_import()['diseaseid'].tolist()
		# distinct_diseases = []
		# for i in keys:
		  # if i not in distinct_diseases:
			# distinct_diseases.append(i)
		# return distinct_diseases
  
	# def pmid_list(self):
		# pmids = self.dataframe.data_import()['pmid'].tolist()
		# return pmids[0:3]

	# def disease_pmid(self):
		# keys = self.dataframe.data_import()['diseaseid'].tolist()
		# pmids = self.dataframe.data_import()['pmid'].tolist()
		# distinctdiseases = dataframe_disease.disease_list()
		# v = []
		# d = {}
		# for j in distinctdiseases: 
            # for i in range(len(keys)):
                # if keys[i] == j: 
                  # v.append(pmids[i])
                  # if j not in d:
                    # d[j] = v
                  # else:
                    # d[j] += v
        # return d

# #print(dataframe_disease)
# dataframe_disease = Association(disease)
# dataframe_disease.disease_list()
# print(len())
# print((dataframe_disease.pmid_list()))
# print(dataframe_disease.disease_pmid())





# counter = 0
# d3 ={}

# for keys_d1 in dictionary1: #loops over keys in d1
  # for keys_d2 in dictionary2: #loops over keys in d2; so 2 loops because we want to compare everything with everything
    # v = []
    # if dictionary1[keys_d1[0]] == dictionary2[keys_d2[0]]:
        # v.append(dictionary1[keys_d1])
    # else: 
        
    # d3[keys_d1, keys_d2] = keys_d1 #makes another dictionary (d3) with the checked (geneid, diseaseid) pair as keys, and 'matches' as values

# #print(d3)


# for k in sorted(d3, key=lambda k: len(d3[k]), reverse=True): #sorts the values of d3 by length so that the longest value is first, and so on
    # if counter == 10: #counter to make sure it returns the first 10, after which it breaks
        # break
    # counter = counter + 1

# #dict_items = d3.items()

# #first_two = list(dict_items)[:20]
# #print(first_two)

 
# print(f"{counter + 1}. diseaseid {k[0]} and gene {k[1]} are related")
