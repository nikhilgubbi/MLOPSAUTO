#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("sender-mail", "password") 
# message to be sent 
message = "Hey Developer, you need to check your code once. Might be this have some error. "
# sending the mail 
s.sendmail("sender-mail", "developer_mail", message) 
# terminating the session 
s.quit()


# In[ ]:




