from flask import Flask, render_template, request,redirect, url_for
import cgi
from part1 import *
app = Flask(__name__, template_folder='template')

#r = Registry().registry_operations()
#op = Registry().execute_operation()


def myform():
    text = request.form.get('text')
    return text


@app.route('/')
def home_page():
    #operations = registry.keys()
    operations= Registry().name_operations()
    return render_template('home_page.html', title="Home Page", operations=operations)

# @app.route('/input_operation/<name>')
# def input_operation(name):
   # return 'welcome %s' % name


@app.route('/Operation', methods=['GET', 'POST'])
def operation():
    
    my_operation = request.args.get('type')
    if request.method == 'POST':
        user = request.form['searchbox']
        display = Registry().Sentences(user)[str(my_operation)]
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)

    if str(my_operation) == 'RowsColumnsGene' or str(my_operation) == 'RowsColumnsDisease' :
        display = Registry().RowsColumns()[str(my_operation)]
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
    
    elif str(my_operation) == 'ColumnLabelGene' or str(my_operation) == 'ColumnLabelDisease' :
       display = Registry().ColumnLabel()[str(my_operation)]
       return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
       
    elif str(my_operation) == 'DistinctGene' or str(my_operation) == 'DistinctDisease' :
        display = Registry().Distinct()[str(my_operation)]
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
     
    #if request.method == 'POST':
    elif str(my_operation) == 'SentenceGene' or str(my_operation) =='SentenceDisease':
        gene = str(myform())
        #if gene != '':           #metti altre condizioni
        
        #if request.method == 'POST':
        #text = request.form.get('text')
        #user = request.form['searchbox']
        display = Registry().Sentences(gene)[str(my_operation)]
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)

        #display = Registry().Sentences(user)[str(my_operation)]
        #return redirect(url_for(render_template('operation.html', title=my_operation, operation=my_operation, display=display)))
  

        #display = Registry().Sentences(1)[str(my_operation)]
        #print(display)
        #return render_template('operation.html', title=my_operation, operation=my_operation, display=display)

    elif str(my_operation) == 'Merge':
        display = Registry().Merge()[str(my_operation)]
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
        
    

if __name__ == '__main__':
    app.run(debug=True)
