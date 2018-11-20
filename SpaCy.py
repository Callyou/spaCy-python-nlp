
# coding: utf-8

# In[53]:

# import SpaCy library and use the french processing pipeline
import spacy
nlp_fr = spacy.load("fr")


# In[54]:

# for beautiful display
from spacy import displacy


# In[121]:

# text to analyze
text_fr = """
Bonjour Madame Dupont H.,
Je vous confirme votre RDV avec : Monsieur Dupont Henry.
Suivi de :
1.a.Dupont H-P.
1.b.Dupont H-P

2.a.Dupont H P.
2.b.Dupont H P

3.a.dupont h-p.
3.b. dupont h p 

4.a.DUPONT H P.
4.b.DUPONT H P
4.c.DUPONT h p
4.d.Dupont H P
4.e.dupont h P
4.f.dupont H P

5.a.DUPONT Henry-Pierre.
5.b.DUPONT Henry Pierre

6.a.DUPONT HENRY PIERRE.
6.b.DUPONT Henry Pierre
6.c.Dupont Henry Pierre
6.d.dupont Henry Pierre
6.e.DUPONT HENRY P

7.a.Dupont Henry.

8.a.dupont henry.

"""


# In[122]:

# processing the text through the pipeline
doc_fr = nlp_fr(text_fr)


# In[123]:

# print each token and if an entity is recognized, we print the entity type
pers = []
anonymous = text_fr
for token in doc_fr:
    # skip line breaks
    if token.text ==  '\n':
        continue
        
    if token.ent_type_ == "PER":
        pers.append(token.text)
        # print('Word : {0}, , Entity : {1}' .format(token.text, token.ent_type_))
        anonymous = anonymous.replace(token.text, "******")
displacy.render(doc_fr, style='ent', jupyter=True)


# In[124]:

# print the PER found with nice color
colors = {'PER': 'linear-gradient(90deg, #aa9cfc, #fc9ce7)'}
options = {'ents': ['PER'], 'colors': colors}
displacy.render(doc_fr, style='ent', jupyter=True, options=options) 


# In[125]:

# replace PER in the text by ******
print(anonymous)


# In[ ]:

# see for yourself, spacy isn't a magic tool, it needs to be tunes or to add parameters and other lib


# In[ ]:



