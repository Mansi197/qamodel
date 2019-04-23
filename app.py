from flask import Flask, render_template,flash,redirect,url_for,session,request,logging,make_response
from wtforms import Form,StringField,TextAreaField,SelectField,PasswordField,validators,IntegerField,DateField
from passlib.hash import sha256_crypt
from datetime import date
from flask import g
import sqlite3
import datetime

app = Flask(__name__)

now=datetime.datetime.now()


class RegistrationForm(Form):
    mychoices= [('Job Seeker','Job Seeker'),('Job Provider','Job Provider')]
    name= StringField('Name/Company Name',[validators.Length(min=1,max=50)])
    username= StringField('Username',[validators.Length(min=1,max=50)])
    email= StringField('Email',[validators.Length(min=1,max=50)])
    category= SelectField('Category',choices=mychoices)
    password= PasswordField('Password',[validators.DataRequired(),validators.EqualTo('confirm',message='Password do not match')])
    confirm= PasswordField('Confirm Password',[validators.Length(min=1,max=50)])
    

class AddJobForm(Form):
    title=StringField('Job Title',[validators.Length(min=1,max=50)])
    location=StringField('Job Location',[validators.Length(min=1,max=50)])
    mychoices= [('Regular','Regular'),('Internship','Internship')]
    category=SelectField('Category',choices=mychoices)
    jobt= [('Work from home','Home'),('On-site','Onsite'),('Part-time','Part')]
    jobtype=SelectField('Job Type',choices=jobt)
    pref=[('Architecture','Architecture'),('Interior Design','Interior Design'),('Commerce','Commerce'),('Accounts','Accounts'),('Chartered Accountancy','Chartered Accountancy'),('Animation','Animation'),('Fashion Design','Fashion Design'),('Graphic Design','Graphic Design'),('Merchandise Design','Merchandise Design'),('Engineering','Engineering'),('Aerospace','Aerospace'),('Biotech','Biotech'),('Chemical','Chemical'),('Civil','Civil'),('Electrical','Electrical'),('Electronics','Electronics'),('Energy Science and Engineering','Energy Science and Engineering'),('Engineering Design','Engineering Design'),('Engineering Physics','Engineering Physics'),('Game Development','Game Development'),('Image Processing','Image Processing'),('Material Science','Material Science'),('Mechanical','Mechanical'),('Metallurgy','Metallurgy'),('Mobile App Development','Mobile App Development'),('Naval and Ocean','Naval and Ocean'),('Petroleum Engineering','Petroleum Engineering'),('Programming','Programming'),('Software Development','Software Development'),('Software Testing','Software Testing'),('Web Development','Web Development'),('Hospitality','Hospitality'),('Hotel Management','Hotel Management'),('Travel and Tourism','Travel and Tourism'),('MBA','MBA'),('Digital Marketing','Digital Marketing'),('Finance','Finance'),('General Management','General Management'),('HR','HR'),('Market Business Research','Market Business Research'),('Marketing','Marketing'),('Operations','Operations'),('Sales','Sales'),('Strategy','Strategy'),('Supply Chain Management','Supply Chain Management'),('Media','Media'),('Cinematography','Cinematography'),('Content Writing','Content Writing'),('Film Making','Film Making'),('Journalism','Journalism'),('Motion Graphics','Motion Graphics'),('Photography','Photography'),('PR','PR'),('Social Media Marketing','Social Media Marketing'),('Video Making Editing','Video Making Editing'),('Videography','Videography'),('Science','Science'),('Biology','Biology'),('Chemistry','Chemistry'),('Mathematics','Mathematics'),('Physics','Physics'),('Statistics','Statistics'),('Others','Others'),('Acting','Acting'),('Agriculture and Food Engineering','Agriculture and Food Engineering'),('Company Secretary','Company Secretary'),('Data Science','Data Science'),('Event Management','Event Management'),('Humanities','Humanities'),('Law','Law'),('Medicine','Medicine'),('Pharmaceutical','Pharmaceutical'),('Psychology','Psychology'),('Teaching','Teaching'),('UI UX','UI UX'),('Volunteering','Volunteering')]
    preference=SelectField('Preference',choices=pref)
    deadline=DateField('Deadline (YYYY/MM/DD)',format="%Y/%m/%d")
    joindate=DateField('Joining Date (YYYY/MM/DD)',format="%Y/%m/%d")
    duration=StringField('Job Duration')
    description=StringField('Job Description',[validators.Length(min=1,max=1000)])


class SeekerRegistrationForm(Form):
    mychoices= [('Male','Male'),('Female','Female')]
    mychoice1=[('Under Graduate','Under Graduate'),('Graduate','Graduate'),('Post Graduate','Post Graduate'),('Doctrate','Doctrate')]
    gender= SelectField('Gender',choices=mychoices)
    degree= SelectField('Degree',choices=mychoice1)
    contact = IntegerField('Contact',[validators.DataRequired()])
    cvlink= StringField('CV Link',[validators.optional()])

class ProviderRegistrationForm(Form):
    power=IntegerField('Man Power',[validators.DataRequired()])
    description= TextAreaField('Job description',[validators.Length(min=1, max=2000)])
    contact = IntegerField('Contact',[validators.optional()])    

# login a user
@app.route('/submit',methods=['GET','POST'])
def login():
    answer=""
    if request.method == 'POST':
        context=request.form['context']
        question=request.form['question']
        print(context,question)
        answer="answer is here"
        return render_template("start.html",context=context,question=question,answer=answer)
    else:
        context=""
        question=""
        return render_template("start.html",context=context,question=question,answer=answer)
#     if request.method == 'POST':
#         username=request.form['username']
#         password=request.form['password']
#         valid = False
#         db=get_db()
#         cur=db.cursor()
#         cur.execute("SELECT count(*) FROM USER WHERE USERNAME=?",[username])
#         count = cur.fetchall()
#         count_num=1
#         row=count[0]
#         if row[0] == 0:
#             count_num=0
#         cur.execute("SELECT * FROM USER WHERE USERNAME=?",[username])
#         data = cur.fetchall()
#         if count_num == 1:
#             row=data[0]
#             hash1 = row[4]
#             valid = sha256_crypt.verify(password,hash1)
#             if valid == True:
#                 session['username'] = username
#                 usertype=row[3]
#                 if usertype == "Job Seeker":
#                     return redirect(url_for('seeker'))
#                 else:
#                     if usertype == "Job Provider":
#                         return redirect(url_for('provider'))
#                     else:
#                         return redirect(url_for('admin'))
        #     else:
        #         flash('Invalid Username or Password')
        # else:
        #     flash('Invalid Username')
    # return redirect(url_for('index'))


@app.route('/')
def index():
    context=""
    answer=""
    question=""
    return render_template('start.html',context=context,question=question,answer=answer)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.secret_key='1234'
    app.run(debug=True)
    