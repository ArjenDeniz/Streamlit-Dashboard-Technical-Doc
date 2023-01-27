# Streamlit Dashboard Technical Document

This document is meant to be a guideline for any dashboard creation by Streamlit. Anyone can add more information by [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), or ask question/define problems through [issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues).

# Requirements

```
streamlit==1.9.0 
pandas
streamlit-echarts
streamlit-option-menu
```

## Streamlit

Be careful of the streamlit version, you are using!

If you have trouble on having same filter keys or broken option-menu, the streamlit versiyon may be different than 1.9.0. 

## Streamlit-option-menu

It is a better looking option-menu then the original. It is quite easy to use and change as described in its [docs.](https://github.com/victoryhb/streamlit-option-menu) 

Only problem is the icon library, some works some doesn’t. Work with caution.

## Streamlit-echarts

Echarts is an open source JS visualization library with incredible amount of different design and style graphics. The advantage of echarts are

- high number of graph option
- Nearly full customizable graphs
- Option to create your responsiveness to the graphs

 However they are also 

- complex to get use to
- Needs a JS & JSON knowledge to use some of the options.

Therefore an alternative should be found in the future for basic reports that does not need complex graph options or styles. (will be discussed under future discussions)

### How to use it

[Streamlit-echarts](https://github.com/andfanilo/streamlit-echarts) is working like a converter, use dictionaries for any json relationship you see in e-charts examples. For any change on graph itself focus on [e-charts docs.](https://echarts.apache.org/en/api.html#echarts) 

Be careful: If there is a problem of generating a graph, problem is probably about the dict relations.

### How to make it responsive

You can set breaking points and styles for each break such as  

![A media sequence to change font sizes after 400px](Streamlit%20Dashboard%20Technical%20Document%20291e1f0953a5476db9cc5f3c465a2702/Untitled.png)

A media sequence to change font sizes after 400px

Be careful, the width defined in e-charts are not the screen size its graph size.

you can look for more detail under its [own document](https://echarts.apache.org/en/api.html#echarts).

# Tips

## **Defining base theme**

Streamlit is an otomatically dual theme site generator, which means that the applications made by it has 2 theme options: light and dark. If you have only one style of design, change the base theme of the system. Otherwise it will change colours according to user’s preference.

To do that create a *****.streamlit***** folder and create a *****************config.toml***************** file. 

![Untitled](Streamlit%20Dashboard%20Technical%20Document%20291e1f0953a5476db9cc5f3c465a2702/Untitled%201.png)

Inside the file wrote as 

```markdown
[theme]
base="light"
```

for only light design.

## **Use functions even for st.markdown**

Do not copy and paste. I repeat do not copy and paste anything that you use more than once. This applies to anything from loading data, data manipulation or creating graphs and even your own design writings. When time comes to change them (several times) you will have hard time implementing on every single one of them. 

### Creating functions for st.markdown

You will need to implement given designs for chapter/sub-chapter names, comments etc. To be able to implement same design without copying you can call st.markdowns as below

```python
def call_barComment(name):
    st.markdown(f"""<div class="CommentBar XS-Margin">
    <p class ="S-Padding">{name}</p>
    </div>""", unsafe_allow_html=True)
```

- Use f before “”” to be able to call any variable from outside
- Use unsafe_allow_html = True to be able to use your own CSS and html,

### Using @st.cache

It is quite easy to cache any function you desire. Only put @st.cache before the function definition. Caching any function that is called several times with same inputs would increase the speed of the site. 

![Untitled](Streamlit%20Dashboard%20Technical%20Document%20291e1f0953a5476db9cc5f3c465a2702/Untitled%202.png)

Note: especially use for loading data on several pages!!.

You can check the **Templates** for filter and graph examples.

## **Applying CSS on the streamlit template**

if you want to change how the header looks or footer or anything that is not created by st.markdowns you need to cheat a bit. 

1. Find the part you want to delete

![Streamlit otomated footer](Streamlit%20Dashboard%20Technical%20Document%20291e1f0953a5476db9cc5f3c465a2702/Untitled%203.png)

Streamlit otomated footer

1. Right click and select inspect element

![google developer console](Streamlit%20Dashboard%20Technical%20Document%20291e1f0953a5476db9cc5f3c465a2702/Untitled%204.png)

google developer console

1. Find the class name of the element

![Untitled](Streamlit%20Dashboard%20Technical%20Document%20291e1f0953a5476db9cc5f3c465a2702/Untitled%205.png)

1. In your css you can change it by calling the class name

```css
.**classname**{
	**your style change**
}
```

Be careful if the style change that you implemented did not shown, use “ !important” after your argument(s). 

# Structure

Basic structure to be implemented from the start should be like

- Data
- Images
- Pages
    - chapter1.py
    - chapter2.py
    - functions.py
    - generalStyle.py
- dashboard.py

To start with basics, load all data on same folder for easier respective path. Same for images.

## Dashboard.py

This is the main file where the actual app is working. Therefore this is the place where you create the option-menu and call for the pages and define st.page_config. 

Do not forget to define a icon in st.page_config as such

![Untitled](Streamlit%20Dashboard%20Technical%20Document%20291e1f0953a5476db9cc5f3c465a2702/Untitled%206.png)

After you call option-menu, you can create each page in the menu separately as in the below example.

![Untitled](Streamlit%20Dashboard%20Technical%20Document%20291e1f0953a5476db9cc5f3c465a2702/Untitled%207.png)

where you defined each page in separate file by defining *************create_page()************* function.

Be careful, you only need to call style in the Dashboard. It will implement on all pages if you use a one liner in every page as 

```python
from dashboard import *
```

## Pages

for each page the structure should be similar to

```python
from .functions import *
from dashboard import *

def create_page():
	#all of the page structure inside
	return True
```

## Functions.py

in this file, every repetative process talked in tips about functions must be implemented. For example each st_markdown that is used more than 1 must be created here so that any change in the function affects all pages. 

Note: A more structured functions folder can be created in the future.

## generalStyle.py

basic structure should be similar to

```python
def create_style():
	styl= """
	* meta tag, font links*
	* all css inside *
	"""
	return styl
```

Implement every design choice here.

- you can write it as you are inside <head></head> brackets.
- You can write any design choice here, so that you do not repeat yourself at every st.markdown.
- After this implementation of design you do **not** need to create <head></head> brackets or CSS in any st.markdown.

# Deployment

Even though there are several options as seen [here.](https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud) We are currently using EC2 as explained in [this article](https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3). It is easy to implement therefore the details will not be explained here. 

Do not forget to create your EC2 in the correct region.

# Templates

# Future Discussions

There are several aspects that can be improved but priorities must be defined more clearly before any improvement.

## Requirements

### *Problems*

- streamlit version problems must be found & solved to use new improvements on streamlit.
- option-menu is deteriorated a new solution may be necessary in the future
- A better understanding of e_charts improves the capabilities
    - An example case: We used for loops for coloring while it somehow accepts list of colors as an input.

### *Improvement areas*

- As an alternative for echarts; faster, easier to create graph library
- A way to create sub-options in the menu

## Structure

For easier to return-read-share-improve-workTogether apps a more readable structure must be implemented. Functions can be divided into more files where each one works on a given concept/area such as only design functions, only data manipulation etc. 

Much more important non-existing structure is on CSS. A more divided design must be used as such long files are un-workable. **A way to implement SCSS** must be searched so that a more responsive designs should be implemented without unnecessary definitions.

 

- A structured functions design
- A way to implement SCSS
- Structured CSS files
- A better way to call images than base64

## Deployment

- How to deploy on azure?
- A cheaper deployment suggestion for bigger projects that need more process power or connection count.