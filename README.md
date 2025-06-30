
## Introduction
**TADAIE** (TOEFL Academic Discussion AI Evaluation Project) 
    is a developing project with a similar **writing page** and an accurate **AI evaluation system** ,which aids TOTFL test taker to utilize murtured AI comment to address existing problems and to improve his/her writing skills within **1 minute**.


## Get it running!
This project is based on **python**, so please insure that python3 has been properly installed.

**Installing Dependenties**

- moudle: **openai**
```cmd
pip install openai
```
- moudle: **flask**
``` cmd
pip install flask
```

**Deepseek API_KEY issue**
Since this project relies on **Deepseek**, so it's necessary to have a vaild **Deepseek API_KEY**, if you've already had one, set the value of system environment *OPENAI_API_KEY* as your own api_key. If you don't have one, go to **https://platform.deepseek.com/api_keys** to register one and set the system environment. 

**Evaluating cost**
 **less than 0.01** Chinese yuan for *deepseek-chat*, **0.06 Chinese yuan** for *deepseek-reasoner(default option for a more accurate score)*


After these steps, run **app.py**, after a few seconds, enter the website in the message (typically http://127.0.0.1:5000). You'll see three sperate information frame and a writing frame.


## Begin to use!

- First, choose a proper paper in the top selector, after questions appear, click <p style="color:blue; border: 4px soild">'Confirm paper and Restart'</p> The timer will restart.

- Then, start composing your article, after finishing, click <p style="color:blue; border: 4px soild">'Submit'</p>You need to wait for about one minute(Maybe a process bar will be add later :) ), and the report will appear, click the word: *"Download Report · HTML Version"* to download the report(Maybe a PDF version will be available soon :) )

## key codes
- If **debug:True** is in your response, then it'll return a fixed, pre-generated report, which is convenient to debug and add new features without consuming usage of your API.

- If **AllowOvertime:True** is in your response, then even if time is over, it won't submit automatically. Submission only occur when the 'Submit' button is clicked.
