# part1
import part2
from abc import ABC, abstractmethod
import pandas as pd
from typing import Set


class ImportDisease:

    def __init__(self, requested_operation, operations=(part2.RowsColumns, part2.ColumnLabel, part2.Distinct, part2.Sentence), datagene="disease_evidences.tsv"):
        self.__df = pd.read_csv(datagene, delimiter="\t")
        self.__operations = operations
        self.requested_operation = str(requested_operation)

    def operation(self):
        for op in self.__operations:
            if str(op) == self.requested_operation:
                operation = op(self.__df)
                result = operation.execute()
                return result


class ImportGene:

    def __init__(self, requested_operation, operations=(part2.RowsColumns, part2.ColumnLabel, part2.Distinct, part2.Sentence), datagene="gene_evidences.tsv"):
        self.__df = pd.read_csv(datagene, delimiter="\t")
        self.__operations = operations
        self.requested_operation = str(requested_operation)

    def operation(self):
        for op in self.__operations:
            if str(op) == self.requested_operation:
                operation = op(self.__df)
                result = operation.execute()
                return result

    def input_operation(self, value):
        for op in self.__operations:
            if str(op) == self.requested_operation:
                operation = op(self.__df)
                result = operation.execute_input(value)
                return result


registry = {'RowsColumnsGene': ImportGene(part2.RowsColumns).operation(),
            'RowsColumnsDisease': ImportDisease(part2.RowsColumns).operation(),
            'ColumnLabelGene': ImportGene(part2.ColumnLabel).operation(),
            'ColumnLabelDisease': ImportDisease(part2.ColumnLabel).operation(),
            'DistinctGene': ImportGene(part2.Distinct).operation(),
            'DistinctDisease': ImportDisease(part2.Distinct).operation(),
            'SentenceGene': ImportGene(part2.Sentence)}