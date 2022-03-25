from flask import Flask, render_template, request,redirect, url_for
from part1 import *
app = Flask(__name__, template_folder='template')


@app.route('/')
def home_page():
    operations= Registry().name_operations()
    op_input = Registry().name_operations_input()
    return render_template('home.html', operations = operations, op_input = op_input)
    
@app.route('/operation_SentenceGene')
def SentenceGene():
    return render_template('Sentencegene.html')

    
@app.route('/operation_SentenceGene', methods=['POST'])
def sentence_gene():
    value = request.form['value']
    display = Registry().Sentences(value)[str('SentenceGene')]
    return render_template('Sentencegene.html', display=display)

@app.route('/operation', methods=['GET'])
def operation():
    
    my_operation = request.args.get('type')
    

    if str(my_operation) == 'RowsColumnsGene' or str(my_operation) == 'RowsColumnsDisease' :
        display = Registry().RowsColumns()[str(my_operation)]
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
    
    elif str(my_operation) == 'ColumnLabelGene' or str(my_operation) == 'ColumnLabelDisease' :
       display = Registry().ColumnLabel()[str(my_operation)]
       return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
       
    elif str(my_operation) == 'DistinctGene' or str(my_operation) == 'DistinctDisease' :
        display = Registry().Distinct()[str(my_operation)]
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
     
  
    # else str(my_operation) == 'Merge':
         # display = Registry().Merge()[str(my_operation)]
         # html = display.to_html()
        
         # text_file = open("index.html", "w")
         # text_file.write(html)
         # text_file.close()
         # return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
      
      
#display = Registry().Sentences(1)#[str('SentenceGene')] 
#print(display)

if __name__ == '__main__':
    app.run(debug=True)
