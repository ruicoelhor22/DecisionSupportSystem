# DecisionSupportSystem
This project is a Decision Support System that aims to help choose the best car model to rent, based on the users inputs. 

It uses a simple Decision Table (or Decision Tree) created on a software called DecisionRules.io, where the models and features are combined. Later, this is accessed via it's API, in order to get a reponse to the best recommended car model to rent.

This is implemented using a flask app in Python, that calls an HTML interface. In this interface, users can insert the inputs needed and than they get a repsonse from the DecisonRules.io API. All of this is paired with a call to the Google Cutom Search API and a Custom Search Engine, in order to get an image of the selected car from Google browser. 

![image](https://github.com/ruicoelhor22/DecisionSupportSystem/assets/58275291/b21cfdcc-834f-4f0c-92d8-cda0fd348c2f)

