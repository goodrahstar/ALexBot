# ALexBot
Alexa on RaspberryPi
###Purpose
I have integrated the Amazon Alexa with RaspberryPi 2 and also have created a software button to invoke the voice command.

###Requirements
You will need:
- A Raspberry Pi
- An SD Card with a fresh install of Raspbian (tested against build Ubuntu)
- A USB headphone

Next you need to obtain a set of credentials from Amazon to use the Alexa Voice service, login at http://developer.amazon.com and Goto Alexa then Alexa Voice Service You need to create a new product type as a Device, for the ID use something like AlexaPi, create a new security profile and under the web settings allowed origins put http://localhost:5000 and as a return URL put http://localhost:5000/code you can also create URLs replacing localhost with the IP of your Pi eg http://192.168.1.123:5000 Make a note of these credentials you will be asked for them during the install process

###Process
- Edit the creds.py file with your credidentials.
- Execute ./setup.sh 
- Execute main.py
- Execute speak.py in separate console, It will record your voice for 7 seconds and will send it to the Alexa.

Now wait for the response from alexa and invoke speak.py as software button.

###TODO
- Automate the voice recording duration.
- Integrate with Face Detection or Voice detection.
