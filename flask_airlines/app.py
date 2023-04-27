import sqlite3
from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/db")
def test_db():
    conn = sqlite3.connect('database.db')   
    print('Opened database successfully', flush=True)
    conn.execute('DROP TABLE IF EXISTS signup')
    conn.commit()
    conn.execute('CREATE TABLE signup (firstname TEXT,lastname TEXT,dob DATE,gender TEXT,contactNumber Number,password PASSWORD)')
    print('Table created successfully', flush=True)
    conn.close()
    return "Table created successfully"

@app.route('/addrec', methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            firstname = request.form['firstName']
            lastname = request.form['lastName']
            dob = request.form['dob']
            gender = request.form['gender']
            contactNumber = request.form['contactNumber']
            password = request.form['password']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor() 
                cur.execute("INSERT INTO signup (firstname,lastname,dob,gender,contactNumber,password) VALUES (?,?,?,?,?,?)", (firstname,lastname,dob,gender,contactNumber,password))

                con.commit()
                msg="Record successfully added"

        except:
                con.rollback()
                msg = "error in insert operation"
        finally:
                con.close()
                return render_template("result.html", msg=msg)
@app.route('/list')
def list():
    con=sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from signup")

    rows = cur.fetchall();
    return render_template("list.html",rows=rows)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        pass
    return render_template('search.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/tnc")
def tnc():
    return render_template("tnc.html")

@app.route("/tq")
def tq():
    return render_template("tq.html")

@app.route('/addflight', methods=['GET', 'POST'])
def addflight():
    if request.method == 'POST':
        pass
    return render_template('addflight.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        pass
    return render_template('checkout.html')

@app.route("/dbase")
def testing_db():
    conn = sqlite3.connect('database.db')   
    print('Opened database successfully', flush=True)
    conn.execute('DROP TABLE IF EXISTS payments')
    conn.commit()
    conn.execute('CREATE TABLE payments (cardNumber NUMBER,mail TEXT,expiryDate DATE,cvv NUMBER,nameOnCard TEXT)')
    print('Table created successfully', flush=True)
    
    conn.close()

    return "Table created successfully"

@app.route('/addcheck', methods = ['POST','GET'])
def addcheck():
    if request.method == 'POST':
        try:
            cardNumber = request.form['card-number']
            mail = request.form['mail']
            expiryDate = request.form['expiry-date']
            cvv = request.form['cvv']
            nameOnCard = request.form['name-on-card']
            

            with sqlite3.connect("database.db") as con:
                cur = con.cursor() 
                cur.execute("INSERT INTO payments (cardNumber,mail,expiryDate,cvv,nameOnCard) VALUES (?,?,?,?,?)", (cardNumber,mail,expiryDate,cvv,nameOnCard))

                con.commit()
                msg="Record successfully added"

        except:
                con.rollback()
                msg = "error in insert operation"
        finally:
                con.close()
                return render_template("result.html", msg=msg)
        
@app.route('/check')
def check():
    con=sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from payments")

    rows = cur.fetchall();
    return render_template("check.html",rows=rows)


@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    if request.method == 'POST':
        pass
    return render_template('thankyou.html')
