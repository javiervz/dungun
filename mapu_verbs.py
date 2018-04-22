
# coding: utf-8

# # Conjugador de verbos en mapudungun
# ## Proponemos dos funciones principales
# ## (1) dado un verbo en infinitivo, conjugamos el verbo en presente (o pasado) en todas las personas gramaticales
# ## (2) dado un verbo conjugado, identificamos la persona y el tiempo verbal
# 
# ### Para lograr esto, disponemos de un diccionario de verbos, lo que nos entrega el significado en espanol. En el caso de palabras OOV, nos basamos unicamente en la morfologia. 

# # (1) verbo en espanol a verbo conjugado en mapudungun

# In[1]:


import pandas as pd


# ### personas gramaticales

# In[2]:


personas={'singular':{1:'iñche',2:'eymi',3:'fey'},'dual':{1:'iñchiw',2:'eymu',3:'feyengu'},'plural':{1:'iñchiñ',2:'eymün',3:'feyengün'}}


# ### diccionario de verbos

# In[3]:


verbos={'salir':'tripa','decir':'pi','entrar':'kon','tomar mate':'matetu','conversar':'nütramka','subir':'püra','ir':'amu','tomar sopa':'korütu','caminar':'treka','estar':'müle','estudiar':'chillkatu','trabajar':'küdaw','lavar loza':'kücha','despertarse':'trepe','comer pan':'kofketu','barrer':'lepün','bañarse':'müñetu','hablar':'dungu','escuchar':'allkütu','comprar':'ngilla','comer':'inyafütu'}


# ### consonantes

# In[4]:


consonantes=['n','w']


# In[102]:


## verbo en espanol a conjugacion en mapudungun
verbos=pd.read_csv('verbs.csv',header=0,sep='\t')
verbos_esp=[verbo for verbo in verbos.esp]
verbos_mapu=[verbo for verbo in verbos.mapu]
verbos={esp:mapu for (esp,mapu) in zip(verbos_esp,verbos_mapu)}

def verb_to_mapudungun(verb_esp,verbos):
    personas={'singular':{1:'iñche',2:'eymi',3:'fey'},'dual':{1:'iñchiw',2:'eymu',3:'feyengu'},'plural':{1:'iñchiñ',2:'eymün',3:'feyengün'}}
    consonantes=['n','w']
    base=verbos[verb_esp]
    conjugacion={'singular':{1:'(yo) iñche',2:'(tú) eymi',3:'(ella/él) fey'},'dual':{1:'(nosotras/nosotros dos) iñchiw',2:'(ustedes dos) eymu',3:'(ellas/ellos dos) feyengu'},'plural':{1:'(nosotras/nosotros) iñchiñ',2:'(ustedes) eymün',3:'(ellas/ellos) feyengün'}}
    for key in personas.keys():
        if base[-1] in consonantes: ## terminan en consonante
            if key=='singular':
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'ün'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'imi'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'i'
            elif key=='dual':
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'iyu'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'imu'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'ingu'
            else:
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'iyiñ'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'imün'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'ingün'
        elif base[-1]=='i': ## termina en i
            if key=='singular':
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'n'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'mi'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base
            elif key=='dual':
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'yu'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'mu'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'ngu'
            else:
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'iñ'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'mün'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'ngün'
        else: ## en otro caso
            if key=='singular':
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'n'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'ymi'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'y'
            elif key=='dual':
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'yu'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'ymu'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'yngu'
            else:
                for key_per in personas[key].keys():
                    if key_per==1:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'iñ'
                    elif key_per==2:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'ymün'
                    else:
                        conjugacion[key][key_per]=conjugacion[key][key_per]+' '+base+'yngün'
                        
    df=pd.DataFrame(conjugacion)
    df = df[['singular', 'dual', 'plural']]
    
    return df.to_html()


# In[103]:


verb_to_mapudungun('barrer',verbos)

