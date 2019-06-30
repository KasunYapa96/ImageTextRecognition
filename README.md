**Basic Requirements**

1. Python 3.7
2. Flask Framework
3. Google Cloud SDK

*Please go through requirements.txt file for all the requirements.*


**Setup GCP**

Create a project & get an authorized credentials as a *json* file from Google Cloud Console


**How to run this!**
*Initial Steps*

1. Create new project & Install Flask on the local machine
2. Clone the project to the relevant project destination
3. Open {main.py} file
4. Check whether there's any error in the code
-- If Yes, please run command: python -m pip install -r requirements.txt
-- If No, Continue
5. Open the json file and copy it's content to *account_key.json* by replacing the existing data
6. Run following commands 
-- set GOOGLE_APPLICATION_CREDENTIALS=account_key.json
-- python main.py

7. Open **http://127.0.0.1:5000** in your browser & upload any image with Texts
8. Check whether the texts of the images are extracted into the interface: success.html

FYI:
Uploaded image will be moved to *uploads* folder.


