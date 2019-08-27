import smtplib
msg="Hello Python"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('sanketgit@gmail.com','password')
mail.sendmail('sanket_from@gmail.com','sanket_to@gmail.com',msg)
mail.close()