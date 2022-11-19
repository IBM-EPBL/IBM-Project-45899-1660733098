


from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db

app = Flask(__name__)

dsn_hostname = "764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "zbq08626"
dsn_pwd = "yLkrp3euaH5svhfO"
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"
dsn_port = "32536"
dsn_security = "SSL"
dsn = ("DRIVER={0};"
"DATABASE={1};"
"HOSTNAME={2};"
"PORT={3};"
"UID={4};"
"PWD={5};"
"SECURITY={6};").format(dsn_driver,dsn_database,dsn_hostname,dsn_port,dsn_uid,dsn_pwd,dsn_security)
print(dsn)

try:
  conn = ibm_db.pconnect(dsn,"","")
  print("success")
except:
  print(ibm_db.conn_errormsg())

@app.route("/" , methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    sql_stmt = "insert into usertbl values(?,?,?)"
    stmt = ibm_db.prepare(conn, sql_stmt)
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    ibm_db.bind_param(stmt, 1, username)
    ibm_db.bind_param(stmt, 2, password)
    ibm_db.bind_param(stmt, 3, email)
    try:
      ibm_db.execute(stmt)
      return redirect('/')
    except:
      print(ibm_db.stmt_errormsg())

  return render_template('registry.html')


@app.route("/welcome",methods=('GET','POST'))
def loginpage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = "select COUNT(*) from usertbl where username='"+username+"' and password='"+password+"'"
        stmt5 = ibm_db.exec_immediate(conn,query)
        row = ibm_db.fetch_tuple(stmt5)
        if(row[0] ==1 ):
            return redirect("/welred")
    return render_template("welcome.html")

@app.route("/welred",methods=('GET','POST'))
def loginpage1():
  return render_template("welcome.html")

@app.route("/welred" , methods=['GET', 'POST'])
def loginpage2():
  if request.method == 'POST':
    sql_stmt = "insert into addcpt values(?,?)"
    stmt = ibm_db.prepare(conn, sql_stmt)
    title = request.form['title']
    complaint = request.form['complaint']
    ibm_db.bind_param(stmt, 1, title)
    ibm_db.bind_param(stmt, 2, complaint)
    try:
      ibm_db.execute(stmt)
      return redirect('/redirect')
    except:
      print(ibm_db.stmt_errormsg())

  return render_template('welcome.html')

@app.route("/redirect",methods=('GET','POST'))
def loginpage3():
  return render_template("signout.html")

@app.route("/redirect",methods=('GET','POST'))
def loginpage4():
  return render_template("signout.html")

@app.route("/relogin",methods=('GET','POST'))
def loginpage5():
  return render_template("registry.html")


if __name__ == "__main__":
    app.run(debug=True)