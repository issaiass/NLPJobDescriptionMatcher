# NLP Job Description Matcher


<details open>
<summary> <b>Project Highlights<b></summary>

The purpose of the project is to analyze information from a resume based on text, keywords or by a <b>.pdf</b> or <b>.docx</b> document using NLP with Spacy.

We will qualify the resumes based on similarity with the job description and will list the best match

</details>

<details open>
<summary> <b>Using The Application<b></summary>



#### <b>Local Testing</b>
- For testing the application locally just enable a new environment, run the requirements and launch the app.
~~~
    conda create -n stnlp python=3.6
    pip install -r requirements.txt
    conda activate stnlp
    streamlit run app.py
~~~

#### <b>Heroku Deployment</b>
- First, navigate to the project folder.
- Next, you need to have a <b>setup.sh</b> script as listed below
~~~
    mkdir -p ~/.streamlit/
    echo "\
    [server]\n\
    headless = true\n\
    port = $PORT\n\
    enableCORS = false\n\
    \n\
    " > ~/.streamlit/config.toml
~~~
- Next add a <b>Procfile</b> with no extension containing the next lines.  NOTE: The name of the .py application must be changed if your app is named differently.
~~~
    web: sh setup.sh && streamlit run app.py
~~~
- Connect to heroku using your credentials
~~~
    heroku login
    <and_set_your_credentials>
~~~
- Create the app
~~~
    heroku create nlpjobdescriptionmatcher
~~~
- Push the app.  NOTE: depending of the <b>main</b> branch if named <b>main</b> or <b>master</b>.
~~~
    git push heroku main
~~~
- Optional:  Push any changes to the remote repo.
~~~
    git add .
    git commit -m "my awesome message"
    git push -u origin main
~~~

<details open>
<summary> <b>Results<b></summary>

We will made a youtube video later

<p align="center"> </p>
</details>


<details open>
<summary> <b>Issues<b></summary>

- On development, no issues found yet.

</details>

<details open>
<summary> <b>Future Work<b></summary>

- Solve NER (Named Entity Recognizer) with Spacy.

</details>

<details open>
<summary> <b>Contributing<b></summary>

Your contributions are always welcome! Please feel free to fork and modify the content but remember to finally do a pull request.

</details>

<details open>
<summary> :iphone: <b>Having Problems?<b></summary>

<p align = "center">

[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/riawa)
[<img src="https://img.shields.io/badge/telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](https://t.me/issaiass)
[<img src="https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white">](https://www.instagram.com/daqsyspty/)
[<img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />](https://twitter.com/daqsyspty) 
[<img src ="https://img.shields.io/badge/facebook-%233b5998.svg?&style=for-the-badge&logo=facebook&logoColor=white%22">](https://www.facebook.com/daqsyspty)
[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/riawe)
[<img src="https://img.shields.io/badge/tiktok-%23000000.svg?&style=for-the-badge&logo=tiktok&logoColor=white" />](https://www.linkedin.com/in/riawe)
[<img src="https://img.shields.io/badge/whatsapp-%23075e54.svg?&style=for-the-badge&logo=whatsapp&logoColor=white" />](https://wa.me/50766168542?text=Hello%20Rangel)
[<img src="https://img.shields.io/badge/hotmail-%23ffbb00.svg?&style=for-the-badge&logo=hotmail&logoColor=white" />](mailto:issaiass@hotmail.com)
[<img src="https://img.shields.io/badge/gmail-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />](mailto:riawalles@gmail.com)

</p>

</details>

<details open>
<summary> <b>License<b></summary>
<p align = "center">
<img src= "https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg" />
</p>
</details>
