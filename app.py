import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers 


# function to get response from llama2 model
def getllamaresponse(input_text, no_words, blog_style):

    model = CTransformers(model='D:\LLM\Blog generation\llama-2-7b-chat.ggmlv3.q8_0.bin',
                          model_type='llama',config={'max_new_tokens':256, 'temperature':0.01})
    
    template = """
    
    Write a birthday message for my {blog_style} on a concept like {input_text} within {no_words}
    
    """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], template=template)
    response = model(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response
  
      
st.set_page_config(page_title = "Birthday Message Writer", page_icon = 'birthday', layout = 'centered',
                   initial_sidebar_state='auto')

st.header("Generate Birthday Messages!")

input_text = st.selectbox("How do you want your message to be ?",("Lovely", "Genuine", "Romantic", "Casual"), index =0)

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input("No of words")
with col2:
    blog_style = st.selectbox("Writing the message for", ('Dad', 'Mom', 'Girlfriend', 'Boyfriend','relatives'), index = 0)
    
submit = st.button("Generate")
if submit:
    st.write(getllamaresponse(input_text, no_words, blog_style))
