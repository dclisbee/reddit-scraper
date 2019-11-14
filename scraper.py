from selenium import webdriver
import time
import smtplib, ssl

#sends email with links retrieved, if any
#conisists of two methods depending on security/auth
class Mail:
    def mailMe(self, contents):
        #sendLinks = linkGroup
        #content = sendLinks
        email = ''
        password = ''

        content = contents
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        mail.sendmail(email, email, content)
        mail.close()


    def mailMe2(self, contents):
        content = contents
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.sendmail(
            email,
            email,
            content)
        server.quit()



#main method
class RedditCheck:

    #activate bot and associate firefox then load initialized link
    def __init__(self):
        self.bot = webdriver.Firefox()

    def load(self):
        bot = self.bot
        bot.get('https://www.reddit.com/r/leagueoflegends/')
        time.sleep(3)


    #scan for html ref then create a list with the links associated
    def titleContains(self):
        
        bot = self.bot
        titles = bot.find_elements_by_class_name('SQnoC3ObvgnGjWt90zD9Z')
        links = [elem.get_attribute('href') for elem in titles]
        listed = []
        tempDoc = ''
        for i in range(len(links)):
            if '' in links[i]:
                listed.append(links[i])
                #print(links[i])
             
            elif '' in links[i]:
                listed.append(links[i])
                #print(links[i])

            elif '' in links[i]:
                listed.append(links[i])

        return listed

    #scroll x times to load page before scanning
    def tilDeath(self):
        bot = self.bot
        for i in range(1,20):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)



red = RedditCheck()
red.load()
red.tilDeath()
red.titleContains()
mailToSend = red.titleContains()
formattedMail = ', '.join(mailToSend)
Mail().mailMe(formattedMail)
print(formattedMail)
