# part1
import part2
from abc import ABC, abstractmethod
import pandas as pd
from typing import Set


class ImportDisease:

    def __init__(self, requested_operation, operations=(part2.RowsColumns, part2.ColumnLabel, part2.Distinct, part2.Sentence), datadisease="disease_evidences.tsv"):
        self.dfdisease = pd.read_csv(datadisease, delimiter="\t")
        self.operations = operations
        self.requested_operation = str(requested_operation)

    def operation(self):
        for op in self.operations:
            if str(op) == self.requested_operation:
                operation = op(self.dfdisease)
                result = operation.execute()
                return result


class ImportGene:

    def __init__(self, requested_operation, operations=(part2.RowsColumns, part2.ColumnLabel, part2.Distinct, part2.Sentence), datagene="gene_evidences.tsv"):
        self.dfgene = pd.read_csv(datagene, delimiter="\t")
        self.operations = operations
        self.requested_operation = str(requested_operation)

    def operation(self):
        for op in self.operations:
            if str(op) == self.requested_operation:
                operation = op(self.dfgene)
                result = operation.execute()
                return result

    def input_operation(self, value):
        for op in self.operations:
            if str(op) == self.requested_operation: 
                operation = op(self.dfgene)
                result = operation.execute_input(value)
                return result   

class MergeDataset(ImportDisease,ImportGene):
    
    def __init__(self, dfdisease, dfgene, requested_operation, operations=(part2.Merge,part2.Merge)):
        ImportDisease.__init__(self, dfdisease)
        ImportGene.__init__(self, dfgene)
        self.merged_dataset = pd.merge(self.dfdisease,self.dfgene, on = "sentence", how = "inner")
        self.requested_operation = str(requested_operation)
        self.operations = operations
        
        
    def operation(self):
        for op in self.operations:
            if str(op) == self.requested_operation:
                operation = op(self.merged_dataset)
                result = operation.associations()
                return result
    
    
   

#print(MergeDataset("disease_evidences.tsv","gene_evidences.tsv").merge())

# dfdisease = pd.read_csv("disease_evidences.tsv", delimiter="\t")
# dfgene = pd.read_csv("gene_evidences.tsv", delimiter="\t")

# merged_dataset = pd.merge(dfdisease,dfgene, on = ('pmid','sentence', 'nsentence'))


registry = {'RowsColumnsGene': ImportGene(part2.RowsColumns).operation(),
            'RowsColumnsDisease': ImportDisease(part2.RowsColumns).operation(),
            'ColumnLabelGene': ImportGene(part2.ColumnLabel).operation(),
            'ColumnLabelDisease': ImportDisease(part2.ColumnLabel).operation(),
            'DistinctGene': ImportGene(part2.Distinct).operation(),
            'DistinctDisease': ImportDisease(part2.Distinct).operation(),
            'SentenceGene': ImportGene(part2.Sentence).operation(),
            'Merge':MergeDataset("disease_evidences.tsv","gene_evidences.tsv",part2.Merge).operation()}

print(registry)