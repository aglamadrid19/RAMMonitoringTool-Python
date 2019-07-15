# RAM Monitoring Tool in Python
# Run it on a remote server by using the cat command. (bash)

# We will run a script on a remote server that does the following:
# Checks current RAM usage (continuously), if RAM usage goes over certain %
# then we will send an email with a Running Processes Report (sorted).

# Dependencies
# While looking to diferent ways to accomplished our goal I decided to use the ***psutil*** library
# This library is being actively developed, and it supports the following OSs 
# Linux # Windows # macOS # FreeBSD, OpenBSD, NetBSD # Sun Solaris # AIX /// 32-bit and 64-bit
# Python versions are 2.6, 2.7 and 3.4+

# It can not get better than that!.

# Import PSUtil
import psutil, smtplib, ssl, socket, time
from getpass import getpass

# Check RAM, and store it (continuously).
def checkRAM(): 
    ramUsage = psutil.virtual_memory()[2]
    return ramUsage

# Send Email
def sendEmail(SmtpUsername, SmtpPassword, RAMUsage):
    
    # From RealPython https://realpython.com/python-send-email/]
    # Check them out[Recommended]

    host_name = socket.gethostname()

    # SMTP connection settings
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL
    sender_email = SmtpUsername
    password = SmtpPassword

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Email content
    # Do not send the email to me :), change the reciever please.
    receiver_email = "aglamadrid19@gmail.com"
    message = """Subject:{} ram usage is at {}%

        Report is not supperted yet ...
        """.format(host_name, checkRAM())
  
    # Try to log in to server and send email
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    return "Email has been sent!"

def mainFlow():
    # Lets get the SMTP credentials
    getSMTPUsername = input("Please type the Username of your SMTP server: ")
    getSMTPPassword = getpass()

    # Calling checkRAM
    ramUsage = checkRAM()

    # Set your limit here, mine is 90%
    while ramUsage < 90:
        print("RAM is: {}%".format(ramUsage))
        ramUsage = checkRAM()
        # Wait 1 sec before continue with loop
        time.sleep(1)
        continue
    # If loop is ended RAM > 90, send email
    sendEmail(getSMTPUsername, getSMTPPassword, ramUsage)

mainFlow()

# Create RAM usage report and export to HTML (This is not supported YET!!!!!)
# def processReporttoHTML():
    # memoryListReport = []
    # for proc in psutil.process_iter():
    #     #  Dont mention it! Looping though dic containing a tuple, looping through that toople
    #     #  and fetching you the portable(multiplatform) memory value (I couldnt figure out, Im moving on)
    #     try:
    #         pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'memory_info'])
    #         memoryListReport.append(pinfo)
            
                
    #     except psutil.NoSuchProcess:
    #         pass

    # # Write HTML report:
    # reportHTML = open('ramReport.html','w')
    # for dic in memoryListReport:
    #     reportHTML.write(str(dic))
    #     reportHTML.write("<br>")
    

    # reportHTML.close