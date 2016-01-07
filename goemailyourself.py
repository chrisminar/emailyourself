#!/usr/bin/python

# for email
import smtplib

#for example
import os
import os.path
import sys
import time
import datetime

##send email function
##note: you must go into your gmail settings and change it to allow access from insecure sources
def send_email(user,pwd,recipient,subject,body):
    gmail_user = user #string
    gmail_pwd = pwd #string
    FROM = user #string
    TO = recipient #string
    SUBJECT = subject #string
    TEXT = body #string

    #setup message
    message = """\From: %s\nTo: %s\nSubject:%s\n\n%s
    """ % (FROM, " , ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user,gmail_pwd)
        server.sendmail(FROM,TO,message)
        server.close()
        print "successfully sent email"
    except:
        print "Error: unable to send email"


#example
if __name__ == '__main__':
    
    #time whatever you want to do
    startTime = time.time()
    ##do some stuff here, I run some c code
    ######################################################################################
    cuibmFolder = os.path.expandvars("/scratch/src/cuIBM-FSI")#base file path
    sys.path.insert(0,cuibmFolder+'/scripts/python')
    caseFolder = cuibmFolder + '/validation/cylinder/Re40' #where case data is
    execPath = cuibmFolder + '/bin/cuIBM'#where c executable is
    runCommand = "%s -caseFolder %s" % (execPath, caseFolder) #command to run
    print runCommand+"\n"
    os.system(runCommand) #execute c code
    #end doing stuff
    endTime = datetime.datetime.now()
    duration = time.time() - startTime
    #end timing
       
    #setup email
    #######################################################################################
    #setgmail user
    g_user = 'sender@gmail.com'
    
    #tell it your password
    g_pwd = 'yourpassword'
   
    #set email recipient
    recip = 'reciever@gmail.com'
    
    #set email subject
    sub = 'Test subject'
   
    #the body of the email, current comments on how devilishly good looking you are
    #then tells you the duration your stuff took and the time it finished
    bod = 'Hello Beautiful, \nYour code took %s seconds to run and finished on %s/%s/%s at %s:%s' % (duration,endTime.month, endTime.day, endTime.year, endTime.hour, endTime.minute)
    
    #send the email!
    send_email(g_user,g_pwd,recip,sub,bod)
