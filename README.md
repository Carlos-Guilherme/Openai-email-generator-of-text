# Openai-email-generator

This code uses the smtplib library and email.message to send an email containing a philosophical message generated by the OpenAI API. The template chosen to generate the message is "text-davinci-003".

The first step in the code is to define the OpenAI API key and the model to be used. Next, a prompt is defined for the API to generate the desired philosophical message based on examples from Stoic and modern philosophy, about modern times. The API is then called using the provided parameters, and the response is stored in the res variable.

The send_email() function is then defined, which builds the body of the email in HTML, with the philosophical message generated by the API. Then the message is set up with a subject, sender, recipient and content. The sender's password is stored in password.

The smtplib library is used to send the email, connecting to the Gmail SMTP server and authenticating with the sender's credentials. The sendmail() function is used to send the message to the recipient, and a confirmation message is displayed in the console output.

Finally, the send_email() function is called to send the email containing the philosophical message generated by the API.

##
The openai api password is obtained directly from the website: https://platform.openai.com/account/api-keys

And the password to use in the library to send the email cannot be the same as your gmail account password, it must be generated in a specific part called: "app passwords". You can access it through this link: https://myaccount.google.com/u/1/security?hl=en
