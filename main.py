import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import smtplib
import socket
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import wmi
import json
import instaloader
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pyautogui
import PyPDF2
import operator
from twilio.rest import Client
first="zero"
master = "Shoaib"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#it only has two voices 0 contain male voice 1 contain the female voice.
engine.setProperty('voice',voices[0].id)

#fuction to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function for wishing
def wish():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning " + master)
    elif(hour>=12 and hour<17):
        speak("Good Afternoon " + master)
    else:
        speak("Good evening " + master)
    speak("This is Blake at your service . How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")

      audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        speak("Sorry, can you please repeat again")
        query=takeCommand()
    return query

def numbers(a):
    if(a.casefold()=='zero'):
        return 0
    elif(a.casefold()=='one'):
        return 1
    elif(a.casefold()=='two'):
        return 2
    elif(a.casefold()=='three'):
        return 3
    elif(a.casefold()=='four'):
        return 4
    elif(a.casefold()=='five'):
        return 5
    elif(a.casefold()=='six'):
        return 6
    elif(a.casefold()=='seven'):
        return 7
    elif(a.casefold()=='eight'):
        return 8
    elif(a.casefold()=='nine'):
        return 9

def pdfreader():
    speak("Sir please enter the path and name of the pdf")
    name=input("Enter the path and name")
    name=name+".pdf"
    #opening the path for the pdf
    book=open(name,'rb')
    #we have pdfreader, pdf merger, pdf apliter, rotate pdf file pages
    pdfReader= PyPDF2.PdfFileReader(book)
    #etting number of pages
    pages=pdfReader.numPages
    speak(f"Total number of pages are {pages}")
    p=True
    
    while(p):
        speak("sir please enter which page do you want to read")
        conf=takeCommand()
        if 'all' in conf.lower():
            for i in range(pages):
                pg=int(i)-1
                page=pdfReader.getPage(i)
                text=page.extractText()
                speak(text)
            speak("Do you want to read another page")
            conf=takeCommand()
            if 'yes' in conf.lower():
                p=True
            else:
                p=False
        else:
            pg=int(conf)-1
            page=pdfReader.getPage(pg)
            text=page.extractText()
            speak(text)
            speak("Do you want to read another page")
            conf=takeCommand()
            if 'yes' in conf.lower():
                p=True
            else:
                p=False

#closing function
def close(pro):
    t=0
    name=pro
    f=wmi.WMI()
    for process in f.Win32_Process():
        if process.name==name:
            process.Terminate()
            t=t+1
    if t==0:
        speak("Process not found")

#insta bot class for messaging
class bot:
    user=""
    message=""
    def __init__(self, username, password, user, message): 
	    self.username = username 
	    self.password = password 
	    self.user = user 
	    self.message = message 
	    self.base_url = 'https://www.instagram.com/'
	    self.bot = webdriver.Chrome(ChromeDriverManager().install()) 
	    self.login() 

    def login(self):
        self.bot.get(self.base_url) 
        enter_username = WebDriverWait(self.bot, 20).until( 
            expected_conditions.presence_of_element_located((By.NAME, 'username'))) 
        enter_username.send_keys(self.username) 
        enter_password = WebDriverWait(self.bot, 20).until( 
            expected_conditions.presence_of_element_located((By.NAME, 'password'))) 
        enter_password.send_keys(self.password) 
        enter_password.send_keys(Keys.RETURN) 
        time.sleep(5) 

		# first pop-up 
        self.bot.find_element_by_xpath( 
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click() 
        time.sleep(2) 

		# 2nd pop-up 
        self.bot.find_element_by_xpath( 
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()  
        time.sleep(3) 

		# direct button 
        self.bot.find_element_by_xpath( 
            '//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Messenger"]').click() 
        time.sleep(3) 
        

        for i in self.user:
            #clicking pencil icon
            self.bot.find_element_by_xpath( 
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click() 
            time.sleep(4) 
			# enter the username 
            self.bot.find_element_by_xpath( 
                '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i) 
            time.sleep(4) 

			# click on the username 
            self.bot.find_element_by_xpath( 
                '/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button').click() 
            time.sleep(4) 

			# next button 
            self.bot.find_element_by_xpath( 
                '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click() 
            time.sleep(4) 

			# click on message area 
            send = self.bot.find_element_by_xpath( 
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            
			# types message 
            send.send_keys(self.message) 
            time.sleep(4) 

			# send message 
            self.bot.find_element_by_xpath( 
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click() 
            time.sleep(4) 

#insta bot for opening insta
class instabot: 
    def __init__(self, username, password): 
        self.username = username 
        self.password = password 
        self.base_url = 'https://www.instagram.com/'
        self.instabot = webdriver.Chrome(ChromeDriverManager().install())  
        self.login() 

    def login(self):
        self.instabot.get(self.base_url) 

        enter_username = WebDriverWait(self.instabot, 20).until( 
            expected_conditions.presence_of_element_located((By.NAME, 'username'))) 
        enter_username.send_keys(self.username) 
        enter_password = WebDriverWait(self.instabot, 20).until( 
            expected_conditions.presence_of_element_located((By.NAME, 'password'))) 
        enter_password.send_keys(self.password) 
        enter_password.send_keys(Keys.RETURN) 
        time.sleep(3) 

		# first pop-up 
        self.instabot.find_element_by_xpath( 
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click() 
        time.sleep(3) 

		# 2nd pop-up 
        self.instabot.find_element_by_xpath( 
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click() 
        time.sleep(3)

#facebook bot for opening
class facebot:
	def __init__(self, username, password): 
		self.username = username 
		self.password = password 
		self.base_url = 'https://www.facebook.com/'
		self.facebot = webdriver.Chrome(ChromeDriverManager().install()) 
		self.login() 

	def login(self): 
		self.facebot.get(self.base_url)
        #entering the username 
		self.facebot.find_element_by_xpath( 
			'/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(self.username) 
		time.sleep(2) 
        
		#entering the password
		self.facebot.find_element_by_xpath( 
			'/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys(self.password) 
		time.sleep(2) 
		
        #clicking the login button
		self.facebot.find_element_by_xpath( 
			'/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click() 
		time.sleep(2)

#opening whatsapp
class whatsapp:
    def __init__(self):
        #it helps to use the cookies so that no need to scan QR code every time
        option=Options()
        option.add_argument("--user-data-dir=chrome-data")
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        option.add_experimental_option('useAutomationExtension',False)

        driver=webdriver.Chrome('E:\\chromedriver_win32\\chromedriver.exe',options=option)
        driver.maximize_window()
        driver.get('https://web.whatsapp.com/')
        speak("Do you want to send message")
        conf=takeCommand()
        if 'yes' in conf.lower():
            p=whatsappbot()
            p.msend(driver)
            speak("Message sent succesfully")
        
#whatsapp bot for sending messages
class whatsappbot:
    driver=""
    def send(self):
        #it helps to use the cookies so that no need to scan QR code every time
        option=Options()
        option.add_argument("--user-data-dir=chrome-data")
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        option.add_experimental_option('useAutomationExtension',False)

        driver=webdriver.Chrome('E:\\chromedriver_win32\\chromedriver.exe',options=option)
        driver.maximize_window()
        driver.get('https://web.whatsapp.com/')
        time.sleep(4)
        speak("To whom do you want to send message")
        name=input("Enter the name correctly")
        names=[name]
        speak("What message do you want to send")
        message=takeCommand()
        msg=[message]
        driver.find_element_by_xpath( 
            '/html/body/div/div/div/div[3]/div/div[1]/div/label/div/div[2]').send_keys(names)
        time.sleep(3)
        p=driver.find_element_by_xpath( 
            '/html/body/div/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        p.send_keys(Keys.RETURN)
        for joke in msg:
            driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(joke)
            driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
        speak("Do you want close the browser")
        conf=takeCommand()
        if 'yes' in conf.lower():
            driver.close()
    def msend(self,driver):
        time.sleep(4)
        speak("To whom do you want to send message")
        name=input("Enter the name correctly")
        names=[name]
        speak("What message do you want to send")
        message=takeCommand()
        msg=[message]
        driver.find_element_by_xpath( 
            '/html/body/div/div/div/div[3]/div/div[1]/div/label/div/div[2]').send_keys(names)
        time.sleep(2)
        p=driver.find_element_by_xpath( 
            '/html/body/div/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        p.send_keys(Keys.RETURN)
        for joke in msg:
            driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(joke)
            driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
        speak("Do you want close the browser")
        conf=takeCommand()
        if 'yes' in conf.lower():
            driver.close()

class cms: 
    def __init__(self): 
        self.username = ["B18CS077"]
        self.password = ["18cs0776"]
        self.base_url = 'https://cms.kitsw.org/'
        self.cms = webdriver.Chrome(ChromeDriverManager().install()) 
        self.login() 

    def login(self): 
        self.cms.get(self.base_url) 
        #entring roll no
        self.cms.find_element_by_xpath( 
			'/html/body/form/div[3]/table/tbody/tr[1]/td[2]/div/table/tbody/tr[3]/td[2]/input').send_keys(self.username) 
        time.sleep(2) 
        
		#entering password
        self.cms.find_element_by_xpath( 
			'/html/body/form/div[3]/table/tbody/tr[1]/td[2]/div/table/tbody/tr[4]/td[2]/input').send_keys(self.password) 
        time.sleep(2) 
        self.cms.find_element_by_xpath( 
			'/html/body/form/div[3]/table/tbody/tr[1]/td[2]/div/table/tbody/tr[6]/td[2]/input').click() 
        time.sleep(2)
        speak("Do you want to know attendance percentage")
        conf=takeCommand()
        if 'yes' in conf.lower():
            self.cms.find_element_by_xpath( 
                '/html/body/form/div[3]/table/tbody/tr[2]/td[1]/table/tbody/tr[4]/td').click()

            #telling the attendance percent
            atten=self.cms.find_element_by_id("lblpercentage")
            speak("Attendance percent is "+atten.text)

            #telling number of classes held
            ch=self.cms.find_element_by_id("lblworkingdays")
            speak("Total classes held are "+ch.text)

            #telling number of classes present
            cp=self.cms.find_element_by_id("lblpresentdays")
            speak("Total classes present are "+cp.text)

            #telling number of classes absent
            ca=self.cms.find_element_by_id("lblabsenton")
            speak("Absent classes are "+ca.text)


#main program
print("Initializing blake")
speak("Initializing blake...")
wish()
cmd=True
while(cmd):
    query=takeCommand()
    if(query==None):
        continue
    else:
        #wikipedia function
        if 'wikipedia' in query.lower():
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            query = query.replace("tell","")
            query = query.replace("about","")
            query = query.replace("who","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        
        #youtube function
        elif 'youtube' in query.lower():
            url="youtube.com"
            chrome_path='C://Program Files//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            print("what do you like to watch ?")
            speak("what do you like to watch ?")
            search1=takeCommand()
            if 'search' in search1:
                search1=search1.replace("search","")
            if 'for' in search1:
                search1=search1.replace("for","")
            search1=search1.replace(' ','+')
            url=url+"/results?search_query="+search1
            webbrowser.get(chrome_path).open(url,new=0)
        
        #google function
        elif 'google' in query.lower()  or 'find' in query.lower():
            chrome_path='C://Program Files//Google//Chrome//Application//chrome.exe %s'#sets the google chrome path
            search1=query.lower()
            if 'search' in search1:
                search1=search1.replace("search","")
            if 'for' in search1:
                search1=search1.replace("for","")
            search1=search1.replace(' ',"+")
            i=0
            url="https://www.google.com/search?q=" + search1 + "&start=" + str(i)
            webbrowser.get(chrome_path).open(url,new=0)#search for the given query
        
        #news
        elif 'news' in query.lower() or 'headlines' in query.lower():
            query_params = {
            "source": "The Indian Express",
            "sortBy": "top",
            }
            main_url = " http://newsapi.org/v2/top-headlines?country=in&apiKey=33efa52b99e347db9e524846833625e5"
            res = requests.get(main_url, params=query_params)
            open_indianExpress_page = res.json()
            # getting all articles in a string article
            article = open_indianExpress_page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                print(i + 1, results[i])
            speak("how many headlines do you want me to read")
            re=int(takeCommand())
            #count=numbers(re)
            for i in range(re):
                speak(results[i])
            speak("Do you want to know anything more?")
            out=takeCommand()
            if(out.casefold()=='yes'):
                speak("What news do you want to search")
                chrome_path='C://Program Files//Google//Chrome//Application//chrome.exe %s'#sets the google chrome path
                search1=takeCommand()
                search1=search1.replace(' ',"+")
                i=0
                url="https://www.google.com/search?q=news+on+" + search1 + "&start=" + str(i)
                webbrowser.get(chrome_path).open(url,new=0)#search for the given query
            else:
                continue
        
        #music
        elif 'play music' in query.lower():
            songs_dir="E:\\music"
            songs=os.listdir(songs_dir)
            print(songs)
            speak("Which song will you prefer")
            search1=takeCommand()
            search1=search1+".mp3"
            p=-1
            for i in range(len(songs)):
                if(search1.casefold()==songs[i].lower()):
                    p=i
            if(p>=0):
                os.startfile(os.path.join(songs_dir,songs[p]))
            else:
                speak("Sorry there is no song named "+ search1)
            
        #telling time
        elif 'time' in query.lower():
            time1=""
            time=datetime.datetime.now().hour
            if(time<12):
                time1=time1+str(time)+":"+datetime.datetime.now().strftime('%M')+"A.M"
            else:
                time=time-12
                time1=time1+str(time)+":"+datetime.datetime.now().strftime('%M')+"P.M"
            speak(time1)
        
        #telling datea
        elif 'date' in query.lower():
            speak(datetime.datetime.now().strftime('%D'))
        
        #Sending the email
        elif 'email' in query.lower() or 'gmail' in query.lower():
            try:
                msg=MIMEMultipart()
                fromaddress="mdshoaib093@gmail.com"
                msg['From']=fromaddress
                mails={'shoaib':'mdshoaib2187@gmail.com','zoheb':'zohaibuzohaib3@gmail.com','raees':'saad20818@gmail.com','vishnu':'B18CS117@kitsw.ac.in'}
                speak("To whom i should send?")
                to=takeCommand()
                if "send it to" in to.lower():
                    to=to.replace("send it to","")
                if to.lower() in mails:
                    to=mails.get(to.lower())
                    msg['To']=to
                    
                else:
                    speak("sir There is no mail named "+to)
                    speak("Sir please enter the mail id to send the mail")
                    to=input("Enter the mail id")
                    msg['To']=to

                    
                speak("Can you tell me the subject")
                sub=takeCommand()
                if 'subject is' in sub.lower():
                    sub=sub.replace('subject is',"")
                msg['Subject']=sub
                speak("what should i send")
                content=takeCommand()
                msg.attach(MIMEText(content,'plain'))
                speak("Do you want to attach any file")
                pre=takeCommand()
                if 'yes' in pre.lower():
                    speak("Enter the file name with extension")
                    fn=input("Enter the file name with extension")
                    attachment=open(fn,'rb')
                    p=MIMEBase('application','octet-stream')
                    p.set_payload((attachment).read())
                    encoders.encode_base64(p)
                    p.add_header('Content-Disposition', "attachment; filename=%s" %fn )
                    msg.attach(p)
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(fromaddress,'Shoaib@093')
                text=msg.as_string()
                server.sendmail(fromaddress,to,text)
                server.quit()
                speak("EMail is sent successfully")
            except Exception as e:
                print(e)
        
        #opening of notepad++
        elif 'notepad plus plus' in query.lower():
            os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")

        #opening dev c++
        elif 'dev c plus plus' in query.lower():
            os.startfile("C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe")
        
        #opening visual studios
        elif 'visual studios' in query.lower():
            os.startfile("C:\\Users\\mohammed\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        #opening resume
        elif 'resume' in query.lower():
            speak("Do you want to edit or see the resume")
            comm=takeCommand()
            if 'edit' in comm.lower():
                os.startfile("E:\\college\\resumes\\Resume Main.docx")
            else:
                os.startfile("E:\\college\\resumes\\Resume Main.pdf")
        
        #opening paper
        elif 'research paper' in query.lower():
            try:
                os.startfile("E:\\college\\paper\\Middleware Technologies.docx")
            except Exception as e:
                speak("Sorry there is no reserach paper in the given location")
        
        #opening command prompt
        elif 'open command prompt' in query.lower() or 'open cmd' in query.lower():
            os.startfile("C:\\Windows\\system32\\cmd.exe")

        #closing command prompt
        elif 'close cmd' in query.lower() or 'close command prompt' in query.lower():
            speak("Ok sir")
            os.system("exit")
        
        #closing notepad ++
        elif 'close notepad' in query.lower():
            speak("Ok sir")
            close('notepad++.exe')

        #closing devc++
        elif 'close dev' in query.lower() or 'close Dev C++' in query.lower():
            speak("Ok sir")
            close("devcpp.exe")

        #closing google
        elif 'close chrome' in query.lower():
            speak("Ok sir")
            try:
                os.system("taskkill /f /im chrome.exe")
            except Exception as e:
                speak("Chrome is already closed")
        
        #closing visual studio
        elif 'close visual studio' in query.lower():
            speak("Ok sir")
            close("Code.exe")
            
        # finding my location
        elif 'where am i' in query.lower() or 'what is my location' in query.lower():
            try:
                ip=requests.get('https://api.ipify.org').text
                print(ip)
                url='https://get.geojs.io/v1/ip/geo/'+ip+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                country= geo_data['country']
                speak(f"sir iam not sure, but i think we are in {city} in  {country}")
            except Exception as e:
                speak("Sorry sir due to network issues i cant able to tell the location")
                pass
                
        #taking screenshot
        elif 'screenshot' in query.lower():
            speak("With what name i should save the screenshot")
            name=takeCommand()
            speak("sir please hold the screen iam taking the screenshot")
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot is saved")
        
        #checking instagram profile
        elif 'check' in query.lower() and ('instagram' in query.lower() or 'intsa' in query.lower()):
            speak("sir Please enter the user name correctly to check")
            name=input("Enter the name")
            webbrowser.open("www.instagram.com/"+name+"")
            speak("sir here is the profile of the user name"+name)
            time.sleep(5)
            speak("Do you want to download the profile picture of this account?")
            conf=takeCommand()
            if 'yes' in conf.lower():
                mod=instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("Profile pic is downloaded in Main folder")
            else:
                pass

        #opening insta
        elif 'open' in query.lower() and ('instagram' in query.lower() or 'insta' in query.lower()):
            speak("Ok sir")
            instabot('mohammed.shoaib093', 'shoaib123')
            input("Done")
            time.sleep(5)
            speak("Sir here is your insta")
        
        #sending message from insta
        elif ('instagram' in query.lower() or 'insta' in query.lower()) and 'message' in query.lower():
            speak("To whom i should send the message sir")
            name=input("Enter the username correctly")
            names=[name]
            speak("What message do you like to send")
            message=takeCommand()
            bot('mohammed.shoaib093', 'shoaib123',names,message)
            input("Done")
            time.sleep(5)
            speak("Message sent successfully")
            os.system("taskkill /f /im chrome.exe")

        #opening facebook
        elif 'open' in query.lower() and ('facebook' in query.lower() or 'fb' in query.lower()):
            speak("Ok sir")
            name=["9704932187"]
            password=["shoaib123"]
            facebot(name,password)
            time.sleep(5)
            speak("Sir here is your facebook")

        #opening whatsapp
        elif 'open' in query.lower() and 'whatsapp' in query.lower():
            speak("Ok sir")
            whatsapp()
            time.sleep(2)
            speak("Sir here is your whatsapp")
        
        #sending message through whatsapp
        elif 'send' in query.lower() and 'whatsapp' in query.lower() and 'message' in query.lower():
            speak("Ok sir")
            wa=whatsappbot()
            wa.send()
            speak("Your message is sent successfully")
        
        #opening cms
        elif 'open' in query.lower() and ('cms' in query.lower() or 'student portal' in query.lower()):
            speak("Ok sir")
            cms()
            time.sleep(5)
            speak("Here is your cms")

        #reading pdf
        elif ('read' in query.lower() or 'reading' in query.lower()) and 'pdf' in query.lower():
            pdfreader()

        #calculations
        elif 'calculate' in query.lower():
            try:
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Yes sir what do you want me to calculate")
                    print("Listening")
                    r.adjust_for_ambient_noise(source)
                    audio=r.listen(source)
                prob=r.recognize_google(audio)
                print(prob)
                if 'divided by' in prob.lower():
                    prob=prob.replace(' by',"")
                def get_operator_fn(op):
                    return{
                        '+' : operator.add, #plus
                        '-' : operator.sub, #minus
                        'x' : operator.mul, #multiplied by
                        'divided' : operator.__truediv__, #divided
                        }[op]
                def eval_binary_expr(op1, oper,op2):
                    op1=int(op1)
                    op2=int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("The result of "+prob+" is")
                speak(eval_binary_expr(*(prob.split())))
            except Exception as e:
                speak("Sir i can not able to understand can u please repeat")
        
        #volumeup
        elif 'volume' in query.lower() and ('increase' in query.lower() or 'up' in query.lower()):
            pyautogui.press("volumeup")
        
        #volumedown
        elif 'volume' in query.lower() and ('down' in query.lower() or 'decrease' in query.lower()):
            pyautogui.press("volumedown")
        
        #mute
        elif 'volume' in query.lower() and ('mute' in query.lower() or 'kill' in query.lower()):
            pyautogui.press("volumemute")
        
        #shutting down
        elif "shutdown" in query.lower() and ('system' in query.lower() or 'pc' in query.lower() or 'computer' in query.lower()):
            os.system("shutdown /s /t 5")

        #restarting the system
        elif "restart" in query.lower() and ('system' in query.lower() or 'pc' in query.lower() or 'computer' in query.lower()):
            os.system("shutdown /r /t 5")

        #sleeping of the system
        elif 'sleep' in query.lower():
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        #Quit function
        elif 'quit' in query.lower() or 'exit' in query.lower() or 'terminate' in query.lower():
            cmd=False