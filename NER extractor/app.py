#!/usr/bin/env python
# coding: utf-8

# In[8]:


from flask import Flask,render_template,url_for, request
import spacy
import re
from spacy import displacy
import pandas as pd
nlp= spacy.load('en_core_web_md')


# In[6]:

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    if request.method == 'POST':
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']
        
        doc = nlp(rawtext)
        d = []
        for ent in doc.ents:
            d.append((ent.label_, ent.text))
            df = pd.DataFrame(d, columns=('named entity', 'output'))
            ORG_named_entity=df.loc[df['named entity'] == 'ORG']['output']
            PERSON_named_entity = df.loc[df['named entity'] == 'PERSON']['output']
            GPE_named_entity= df.loc[df['named entity'] == 'GPE']['output']
            PRODUCT_named_entity = df.loc[df['named entity'] == 'PRODUCT']['output']
            LOC_named_entity = df.loc[df['named entity'] == 'LOC']['output']
            WORK_OF_ART_named_entity = df.loc[df['named entity'] == 'WORK_OF_ART']['output']
            MONEY_named_entity = df.loc[df['named entity'] == 'MONEY']['output']
            QUANTITY_named_entity = df.loc[df['named entity'] == 'QUANTITY']['output']
            LANGUAGE_named_entity = df.loc[df['named entity'] == 'LANGUAGE']['output']
            NORP_named_entity = df.loc[df['named entity'] == 'NORP']['output']
            
        if choice == 'organization':
            results = ORG_named_entity
            num_of_results = len(results)
        elif choice == 'person':
            results = PERSON_named_entity
            num_of_results = len(results)
        elif choice == 'geopolitical':
            results = GPE_named_entity
            num_of_results = len(results)
        elif choice == 'product':
            results = PRODUCT_named_entity
            num_of_results = len(results)
        elif choice == 'location':
            results = LOC_named_entity
            num_of_results = len(results)
        elif choice == 'work and art':
            results = WORK_OF_ART_named_entity
            num_of_results = len(results)
        elif choice == 'money':
            results = MONEY_named_entity
            num_of_results = len(results)
        elif choice == 'quantity':
            results = QUANTITY_named_entity
            num_of_results = len(results)
        elif choice == 'language':
            results = LANGUAGE_named_entity
            num_of_results = len(results)
        elif choice == 'nationality':
            results = NORP_named_entity
            num_of_results = len(results)
            
            
    return render_template("index.html", results = results, num_of_results = num_of_results)


if __name__ == '__main__':
    app.run(debug= True)


# In[ ]:




