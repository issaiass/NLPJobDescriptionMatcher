import streamlit as st
import spacy_streamlit 
import spacy
from spacy import displacy
import json

models = ['es_core_news_sm', 'en_core_web_sm']
def displaycy(args):
    text = args
    try:
        nlp = spacy.load(models[0])
    except: # If not present, we download
        spacy.cli.download("en_core_web_md")
    nlp = spacy.load(models[0])
    doc = nlp(text)
    st.header("Visualizador de Partes de Texto")
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    # Display the entity visualization in the browser:
    st.markdown(ent_html, unsafe_allow_html=True)



# Side Bar
with st.sidebar:
    st.title('Analyzer Tool - Options')


    # Radio Button Actions
    analysis_actions = ('Compare with Job Description', 'Extract Info from Resume')
    analysis_type = st.radio("Action", analysis_actions)
    	

    if analysis_type!='Extract Info from Resume':
        # Job Description components
        job_selector_actions = ('Text', 'Keywords', 'File')
        job_selector_type = st.radio("Job Description Options", job_selector_actions)
        if job_selector_type=='Text':
            job_description = st.text_area('Write or paste the Job Description', '')
        if job_selector_type=='Keywords':
            with open('job_descriptions.json', "r") as f:
                json_jobs = json.loads(f.read())
            job_type = st.selectbox(label='Job Type', options=json_jobs['jobs'])
            job_type_descriptions = json_jobs['jobs'][job_type]
            job_description = st.multiselect(label='Job Descriptions', options=job_type_descriptions, default=job_type_descriptions)        
        if job_selector_type=='File':
            job_description = st.file_uploader("Upload the Job Description")
            if job_description is not None:
                # To read file as bytes:
                pass
                #bytes_data = job_description.getvalue()
                #st.write(bytes_data)

    # Resume Components
    resume_selector_actions = ('Text', 'File')
    resume_selector_type = st.radio("Resume Options", resume_selector_actions)
    
    if resume_selector_type=='Text':
        resume_description = st.text_area(label='Write or paste the Resume', value='')
    if resume_selector_type=='File':
        resume_description = st.file_uploader("Choose Resume(s)", accept_multiple_files=True)
        for resume in resume_description:
            pass
            #bytes_data = resume.read()
            #st.write("filename:", resume.name)
            #st.write(bytes_data)


    st.button('Start Analysis', on_click=displaycy, args=(resume_description,))

hide_st_style = """
    <style>
    #MainMenu {visibility:visible;}
    footer {visibility: hidden;}
    </style>
"""




st.markdown(hide_st_style, unsafe_allow_html=True)
