from flask import Flask
from flask import Flask, jsonify, request ,render_template ,render_template_string
app = Flask(__name__)





@app.route('/')
def hello_world():
    f1=open('file1.txt','r')
    
    g1= f1.read().splitlines()
    g1=g1[1:10]
   
    # content = f1.readlines()
    # line = f1.rstrip('\n')
    # print(content[0:3])
    return render_template('view.html',n1=g1)

@app.route('/<fname>',methods=['GET'])
def read_file(fname):
    start = request.args.get('start')
    end = request.args.get('end')
    
    fname=str(fname)
    if fname=='file1.txt':
        f1=open(fname,'r')
    elif fname=='file2.txt':
        f1=open(fname, encoding='utf-16')
    elif fname=='file3.txt':
        f1=open(fname, 'r')
    elif fname=='file4.txt':
        f1=open(fname, encoding='utf-16')

    # g1= f1.read()
    g1= f1.read().splitlines()
    if start and end:
        print(',,,,,,,,,,,,,,,,,,,,')
        g1=g1[int(start):int(end)]
    return render_template('view.html',n1=g1)

@app.route('/all', methods=['POST','GET'])
def all():
    print(',,,,,,,,,,,,,,,,,,,,,,')
    f1=open('file1.txt','r')
    g1= f1.read()
    g1.replace('\n', '<br>')
    f2=open('file2.txt', encoding='utf-16')
    # f2.encode('utf-8').strip()
    g2= f2.read()
    f3=open('file3.txt','r')
    g3= f3.read()
    f4=open('file4.txt',encoding='utf-16')
    g4= f4.read()
    return render_template('view.html',n1=g1,n2=g2,n3=g3,n4=g4)

 



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)