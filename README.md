# USED VEHICLE PRICE PREDICTION

### This is a Machine Learning Model Deployed using Flask in a WebApp currently running on localhost

Clone the repository using ```git clone```

Follow the steps in order to run the webapp in your Desktop. You should have python installed in your device as well as Flask
Once you have Python installed you can install Flask using the following command

```$ pip install flask```

You should create a virtual environment as *virtualenv* in the project folder.  Paste the command in anaconda prompt in order to install virtual environment:

```$ pip install virtualenv```

Now create a virtual environment with the name *env* (say) in the project folder using the following command:

```$ virtualenv env```

Now to activate the virtualenv use: 

```$ env/Scripts/activate.bat```

You have to import all the python Libraries in that virtualenv. The installation commands are pasted below that you should paste in anaconda prompt: 

numpy: 
```$ pip install numpy```
pandas: 
```$ pip install pandas```  
scikit-learn: 
```$ pip install -U scikit-learn```

after installation of the above libraries use the following command to run your flask webapp in the virtual environment (env)

```$ flask run``` 
In anaconda prompt and you will get an https link that you should paste in your browser and in the local host you can access the webpage, then you should provide all the attributes that are asked and finally click the predict button and you will get a predicted probable price according to the Machine Learning Model
